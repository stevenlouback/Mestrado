import json

from flask import Flask, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from numpy import long
from sqlalchemy import engine, func

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/Quimiometria'

db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.errorhandler(404)
def not_found(error):
    print("erro")
    return make_response(jsonify({'error': 'Não existe.'}), 404)

########################################
#Rotas da Tabela Modelo
########################################

from models.model import ModeloCalibracao
from controller.controllerModelo import geraModelo
from controller.controllerPredicao import geraPredicao
from metodos.pls import PLS

@app.route("/modelo/calibra/<id_>/<latente_>/<corte_>/<qtde_>", methods=['POST'])
def calibraModelo(id_, latente_, corte_, qtde_):
    try:
        if (not id_):
            abort(400)

        pls = PLS()
        pls.calibracao(id_, latente_, corte_, qtde_)
        return jsonify({'success': 'OK'}), 201
    except Exception as e:
	      return(str(e))

@app.route('/modelo/adiciona', methods=['POST'])
def create_modelo():
    print('Entrou')
    print(request.json)
    if not request.json or not 'nmmodelo' in request.json:
        abort(400)

    objeto = request.json

    msg = geraModelo(db, objeto)
    db.session.commit()
    return jsonify({'success': msg}), 201

@app.route("/modelo/add")
def add_modelo():
    param = request.args.get('param')
    param = '{'+param+'}'
    objeto = json.loads(param)

    msg = geraModelo(db,objeto)

    db.session.commit()

    #return msg
    modelos = ModeloCalibracao.query.all()
    return jsonify([e.serialize() for e in modelos])
    #return str(ModeloCalibracao.query.all())


@app.route("/modelo/getall")
def get_all():
    try:
        modelos=ModeloCalibracao.query.all()
        return  jsonify([e.serialize() for e in modelos])
    except Exception as e:
	      return(str(e))

@app.route("/modelo/get/<id_>")
def get_by_id(id_):
    try:
        modelo=ModeloCalibracao.query.filter_by(idmodelo=id_).first()
        return jsonify(modelo.serialize())
    except Exception as e:
	      return(str(e))

########################################
#Rotas da Tabela AMOSTRA
########################################

from models.model import Amostra
from controller.controllerAmostra import geraAmostra

@app.route('/amostra/predicao', methods=['POST'])
def predicao_amostra_nova():
    # print(request.json)
    if not request.json or not 'nmidentifica' in request.json:
        abort(400)

    objeto = request.json

    if not 'dsespectro' in request.json:
        objeto['dsespectro'] = None

    modelo = objeto['modelo']
    idmodelo = modelo['idmodelo']

    msg = geraAmostra(db, objeto)
    idamostra= msg

    print('amostra gravada ',idamostra)
    # RECUPERA O JSON DENTRO DE JSON
    # MONTA A MATRIZ Y
    try:
        modelo = MatrizY(
            idmodelo=idmodelo,
            idamostra=idamostra,
            idparametroref=1,
            idcalibracao=None,
            vlresultado=None,
            vlreferencia=None,
            dtpredicao=None
        )
        db.session.add(modelo)
    except Exception as e:
        return (str(e))


    # Access data
    # MONTA A MATRIZ X
    for y in objeto['listaMatrizX']:
        nrsequencia= y['nrsequencia']
        nrposicaolinha = y['nrposicaolinha']
        nrposicaocoluna = y['nrposicaocoluna']
        vllinhacoluna = y['vllinhacoluna']

        if not 'idpixel' in y:
            idpixel=1
        else:
            idpixel=y['idpixel']

        try:
            modelo = MatrizX(
                idmodelo=idmodelo,
                idamostra=idamostra,
                nrsequencia=nrsequencia,
                nrposicaolinha=nrposicaolinha,
                nrposicaocoluna=nrposicaocoluna,
                vllinhacoluna=vllinhacoluna,
                idpixel=idpixel
            )
            db.session.add(modelo)
        except Exception as e:
            return (str(e))

    print('pls')
    pls = PLS()
    pls.predicao(idmodelo,idamostra)
    print('previu')
    db.session.commit()

    return jsonify({'success': msg}), 201


@app.route('/amostra/adiciona', methods=['POST'])
def create_toda_amostra():
    print(request.json)
    if not request.json or not 'nmidentifica' in request.json:
        abort(400)

    objeto = request.json
    modelo = objeto['modelo']
    idmodelo = modelo['idmodelo']

    msg = geraAmostra(db, objeto)
    idamostra= msg

    # RECUPERA O JSON DENTRO DE JSON
    # MONTA A MATRIZ Y
    # Access data
    for x in objeto['listaParametro']:
        idparametroref = x['idparametroref']
        idcalibracao = None
        vlresultado = None
        vlreferencia = x['valorMovto']
        dtpredicao = None
        print(vlreferencia)

        try:
            modelo = MatrizY(
                idmodelo=idmodelo,
                idamostra=idamostra,
                idparametroref=idparametroref,
                idcalibracao=idcalibracao,
                vlresultado=vlresultado,
                vlreferencia=vlreferencia,
                dtpredicao=dtpredicao
            )
            db.session.add(modelo)
        except Exception as e:
            return (str(e))

    # MONTA A MATRIZ X
    for y in objeto['listaMatrizX']:
        nrsequencia= y['nrsequencia']
        nrposicaolinha = y['nrposicaolinha']
        nrposicaocoluna = y['nrposicaocoluna']
        vllinhacoluna = y['vllinhacoluna']

        if not 'idpixel' in y:
            idpixel=1
        else:
            idpixel=y['idpixel']

        try:
            modelo = MatrizX(
                idmodelo=idmodelo,
                idamostra=idamostra,
                nrsequencia=nrsequencia,
                nrposicaolinha=nrposicaolinha,
                nrposicaocoluna=nrposicaocoluna,
                vllinhacoluna=vllinhacoluna,
                idpixel=idpixel
            )
            db.session.add(modelo)
        except Exception as e:
            return (str(e))

    db.session.commit()

    return jsonify({'success': msg}), 201


@app.route("/amostra/add")
def add_amostra():
    param = request.args.get('param')
    objeto = json.loads(param)

    msg = geraAmostra(db, objeto)

    db.session.commit()

    return msg

@app.route("/amostra/getall")
def get_allAmostra():
    try:
        modelos=Amostra.query.all()
        return  jsonify([e.serialize() for e in modelos])
    except Exception as e:
	      return(str(e))

@app.route("/amostra/get/<idmodelo_>/<idamostra_>")
def get_by_idAmostra(idmodelo_,idamostra_):
    try:
        modelo=ModeloCalibracao.query.filter_by(idmodelo=idmodelo_,idamostra=idamostra_).first()
        return jsonify(modelo.serialize())
    except Exception as e:
	      return(str(e))


########################################
#Rotas da Tabela Amostra_Calibracao
########################################

from models.model import AmostraCalibracao
from controller.controllerAmostraCalibracao import geraAmostraCalibracao

@app.route("/amostracalibracao/add")
def add_amostraCalibracao():
    param = request.args.get('param')
    objeto = json.loads(param)

    msg = geraAmostraCalibracao(db, objeto)

    db.session.commit()

    return msg

@app.route("/amostracalibracao/getall")
def get_allAmostraCalibracao():
    try:
        modelos=AmostraCalibracao.query.all()
        return  jsonify([e.serialize() for e in modelos])
    except Exception as e:
	      return(str(e))

@app.route("/amostracalibracao/get/<idmodelo_>/<idamostra_>/<idcalibracao_>")
def get_by_idAmostraCalibracao(idmodelo_,idamostra_,idcalibracao_):
    try:
        modelo=AmostraCalibracao.query.filter_by(idmodelo=idmodelo_,idamostra=idamostra_,idcalibracao=idcalibracao_).first()
        return jsonify(modelo.serialize())
    except Exception as e:
	      return(str(e))


########################################
#Rotas da Tabela CALIBRACAO
########################################

from models.model import Calibracao
from controller.controllerCalibracao import geraCalibracao

@app.route("/calibracao/add")
def add_calibracao():
    param = request.args.get('param')
    objeto = json.loads(param)

    msg = geraCalibracao(db, objeto)

    db.session.commit()

    return msg

@app.route("/calibracao/getall")
def get_allCalibracao():
    try:
        modelos=Calibracao.query.all()
        return  jsonify([e.serialize() for e in modelos])
    except Exception as e:
	      return(str(e))

@app.route("/calibracao/get/<idmodelo_>/<idcalibracao_>")
def get_by_idCalibracao(idmodelo_,idcalibracao_):
    try:
        modelo=AmostraCalibracao.query.filter_by(idmodelo=idmodelo_,idcalibracao=idcalibracao_).first()
        return jsonify(modelo.serialize())
    except Exception as e:
        return (str(e))


@app.route("/calibracao/getAtivo/<idmodelo_>")
def get_by_CalibracaoAtiva(idmodelo_):
    try:
        inativo='A'
        modelo=Calibracao.query.filter_by(idmodelo=idmodelo_,inativo=inativo).first()
        return jsonify(modelo.serialize())
    except Exception as e:
        # print(e)
	      return(str(e))


########################################
#Rotas da Tabela MATRIZ_X
########################################

from models.model import MatrizX

@app.route("/matrizx/add")
def add_matrizx():
    param = request.args.get('param')
    objeto = json.loads(param)

    idmodelo= objeto['idmodelo']
    idamostra=objeto['idamostra']
    nrposicaolinha=objeto['nrposicaolinha']
    nrposicaocoluna=objeto['nrposicaocoluna']
    vllinhacoluna=objeto['vllinhacoluna']

    try:
        modelo=MatrizX(
            idmodelo=idmodelo,
            idamostra=idamostra,
            nrposicaolinha=nrposicaolinha,
            nrposicaocoluna = nrposicaocoluna,
            vllinhacoluna = vllinhacoluna
        )
        db.session.add(modelo)
        db.session.commit()
        return "Matriz X Registrada."
    except Exception as e:
	      return(str(e))

@app.route("/matrizx/getall")
def get_allmatrizx():
    try:
        modelos=MatrizX.query.all()
        return  jsonify([e.serialize() for e in modelos])
    except Exception as e:
	      return(str(e))

@app.route("/matrizx/get/<idmodelo_>/<idamostra_>/<nrsequencia_>")
def get_by_idmatrizx(idmodelo_,idamostra_,nrsequencia_):
    try:
        modelo=AmostraCalibracao.query.filter_by(idmodelo=idmodelo_,idamostra=idamostra_,nrsequencia=nrsequencia_).first()
        return jsonify(modelo.serialize())
    except Exception as e:
	      return(str(e))


########################################
#Rotas da Tabela MATRIZ_Y
########################################

from models.model import MatrizY

@app.route("/matrizy/add")
def add_matrizy():
    param = request.args.get('param')
    objeto = json.loads(param)

    idmodelo= objeto['idmodelo']
    idamostra=objeto['idamostra']
    idparametroref=objeto['idparametroref']
    idcalibracao=objeto['idcalibracao']
    vlresultado=objeto['vlresultado']
    vlreferencia = objeto['vlreferencia']
    dtpredicao = objeto['dtpredicao']


    try:
        modelo=MatrizY(
            idmodelo=idmodelo,
            idamostra=idamostra,
            idparametroref=idparametroref,
            idcalibracao = idcalibracao,
            vlresultado = vlresultado,
            vlreferencia=vlreferencia,
            dtpredicao=dtpredicao
        )
        db.session.add(modelo)
        db.session.commit()
        return "Matriz Y Registrada."
    except Exception as e:
	      return(str(e))

@app.route("/matrizy/getall")
def get_allmatrizy():
    try:
        modelos=MatrizY.query.all()
        return  jsonify([e.serialize() for e in modelos])
    except Exception as e:
	      return(str(e))

@app.route("/matrizy/getallmodelo/<idmodelo_>")
def get_allmatryzymodelo(idmodelo_):
    try:
        modelos=MatrizY.query.filter_by(idmodelo=idmodelo_)
        return  jsonify([e.serialize() for e in modelos])
    except Exception as e:
	      return(str(e))


@app.route("/matrizy/get/<idmodelo_>/<idamostra_>/<idparametroref_>")
def get_by_idmatrizy(idmodelo_,idamostra_,idparametroref_):
    try:
        modelo=MatrizY.query.filter_by(idmodelo=idmodelo_,idamostra=idamostra_,idparametroref=idparametroref_).first()
        return jsonify(modelo.serialize())
    except Exception as e:
	      return(str(e))

########################################
#Rotas da Tabela PARAMETROS
########################################

from models.model import Parametro

@app.route('/parametros/adiciona', methods=['POST'])
def create_parametro():
    print(request.json)
    if not request.json or not 'nmparametroref' in request.json :
        abort(400)

    objeto = request.json

    #RECUPERA O JSON DENTRO DE JSON
    data = objeto['modelo']
    idmodelo= data['idmodelo']


    idparametroref = objeto['idparametroref']
    nmparametroref = objeto['nmparametroref']

    if idparametroref == "":
        idparametroref = (db.session.query(func.max(Parametro.idparametroref)).filter_by(idmodelo=idmodelo).scalar() or 0) + 1

    if idparametroref == 0:
        idparametroref = (db.session.query(func.max(Parametro.idparametroref)).filter_by(idmodelo=idmodelo).scalar() or 0) + 1

    try:
        modelo = Parametro(

            idparametroref=idparametroref,
            idmodelo=idmodelo,
            nmparametroref=nmparametroref
        )

        print(modelo.idmodelo)
        print(modelo.idparametroref)
        print(modelo.nmparametroref)

        db.session.add(modelo)
        db.session.commit()
        msg = "Parametro Adicionado. idmodelo={}".format(objeto.idmodelo)
    except Exception as e:
        msg = e
        abort(400)

    return jsonify({'success': msg}), 201


@app.route("/parametros/add")
def add_parametros():
    param = request.args.get('param')
    objeto = json.loads(param)

    idmodelo= objeto['idmodelo']
    nmparametroref=objeto['nmparametroref']

    # Pega a ultima sequencia para gravar no banco
    idparametroref = (db.session.query(func.max(Parametro.idparametroref)).filter_by(idmodelo=idmodelo).scalar() or 0) + 1

    try:
        modelo=Parametro(
            idparametroref =idparametroref,
            idmodelo=idmodelo,
            nmparametroref=nmparametroref
        )
        db.session.add(modelo)
        db.session.commit()
        return "Parametros Registrado."
    except Exception as e:
	      return(str(e))

@app.route("/parametros/getall")
def get_allparametros():
    try:
        modelos=Parametro.query.all()
        return  jsonify([e.serialize() for e in modelos])
    except Exception as e:
	      return(str(e))

@app.route("/parametros/getallModelo/<idmodelo_>")
def get_allparametrosModelo(idmodelo_):
    try:
        modelos=Parametro.query.filter_by(idmodelo=idmodelo_)
        return  jsonify([e.serialize() for e in modelos])
    except Exception as e:
	      return(str(e))


@app.route("/parametros/getallTipoAmostra/<tpamostra_>")
def get_allTipoAmostraModelo(tpamostra_):
    try:
        modelos=Parametro.query.filter_by(tpamostra=tpamostra_)
        return  jsonify([e.serialize() for e in modelos])
    except Exception as e:
	      return(str(e))

@app.route("/parametros/get/<idmodelo_>/<idparametroref_>")
def get_by_idparametros(idmodelo_,idparametroref_):
    try:
        modelo=Parametro.query.filter_by(idmodelo=idmodelo_,idparametroref=idparametroref_).first()
        return jsonify(modelo.serialize())
    except Exception as e:
	      return(str(e))

########################################
#Rotas da Predição
########################################

@app.route("/predicao/get/<idmodelo>/<idamostra>")
def get_by_amostra(idmodelo, idamostra):
    try:
        pls = PLS()
        resultado=pls.predicao(idmodelo=idmodelo,idamostra=idamostra)
        print(resultado)
        return  resultado
        #return jsonify(resultado.serialize())
    except Exception as e:
	      return(str(e))

@app.route('/predicao/adiciona', methods=['POST'])
def create_predicao():
    if not request.json or not 'valorpredito' in request.json:
        abort(400)

    objeto = request.json

    msg = geraPredicao(db, objeto)
    db.session.commit()
    return jsonify({'success': msg}), 201

if __name__ == '__main__':
    app.run()