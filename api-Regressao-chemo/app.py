import json

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import engine, func

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/Quimiometria'

db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello World!"

########################################
#Rotas da Tabela Modelo
########################################

from models.modelModeloCal import ModeloCalibracao

@app.route("/modelo/add")
def add_modelo():
    param = request.args.get('param')
    objeto = json.loads(param)

    nmmodelo= objeto['nmmodelo']
    nmmetodoreferencia=objeto['nmmetodoreferencia']
    tpinstrumento=objeto['tpinstrumento']
    dsmodelo = objeto['dsmodelo']
    dtcriacao = objeto['dtcriacao']

    try:
        modelo=ModeloCalibracao(
            nmmodelo=nmmodelo,
            nmmetodoreferencia=nmmetodoreferencia,
            tpinstrumento=tpinstrumento,
            dsmodelo=dsmodelo,
            dtcriacao=dtcriacao
        )
        db.session.add(modelo)
        db.session.commit()
        return "Modelo Adicionado. idmodelo={}".format(modelo.idmodelo)
    except Exception as e:
	      return(str(e))

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

from models.modelAmostra import Amostra

@app.route("/amostra/add")
def add_amostra():
    param = request.args.get('param')
    objeto = json.loads(param)

    idmodelo= objeto['idmodelo']
    tpamostra=objeto['tpamostra']
    dsobservacoes=objeto['dsobservacoes']
    dtcoletaamostra = objeto['dtcoletaamostra']

    #Pega a ultima sequencia para gravar no banco
    idamostra = (db.session.query(func.max(Amostra.idamostra)).filter_by(idmodelo=idmodelo).scalar() or 0) + 1

    try:
        modelo=Amostra(
            idmodelo=idmodelo,
            idamostra=idamostra,
            tpamostra=tpamostra,
            dsobservacoes=dsobservacoes,
            dtcoletaamostra=dtcoletaamostra
        )
        db.session.add(modelo)
        db.session.commit()
        return "Amostra Adicionada. idmodelo={}".format(modelo.idmodelo)+" idAmostra={}".format(modelo.idamostra)
    except Exception as e:
	      return(str(e))

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

from models.modelAmostraCalibracao import AmostraCalibracao

@app.route("/amostracalibracao/add")
def add_amostraCalibracao():
    param = request.args.get('param')
    objeto = json.loads(param)

    idmodelo= objeto['idmodelo']
    idamostra=objeto['idamostra']
    idcalibracao=objeto['idcalibracao']

    try:
        modelo=AmostraCalibracao(
            idmodelo=idmodelo,
            idamostra=idamostra,
            idcalibracao=idcalibracao
        )
        db.session.add(modelo)
        db.session.commit()
        return "Amostra da Calibração Adicionada."
    except Exception as e:
	      return(str(e))

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

from models.modelCalibracao import Calibracao

@app.route("/calibracao/add")
def add_calibracao():
    param = request.args.get('param')
    objeto = json.loads(param)

    idmodelo= objeto['idmodelo']
    inativo=objeto['inativo']
    dtcalibracao=objeto['dtcalibracao']

    try:
        modelo=Calibracao(
            idmodelo=idmodelo,
            inativo=inativo,
            dtcalibracao=dtcalibracao
        )
        db.session.add(modelo)
        db.session.commit()
        return "Calibração Registrada."
    except Exception as e:
	      return(str(e))

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
	      return(str(e))


########################################
#Rotas da Tabela MATRIZ_X
########################################

from models.modelMatrizX import MatrizX

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

from models.modelMatrizY import MatrizY

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

from models.modelParametro import Parametro

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

@app.route("/parametros/get/<idmodelo_>/<idparametroref_>")
def get_by_idparametros(idmodelo_,idparametroref_):
    try:
        modelo=Parametro.query.filter_by(idmodelo=idmodelo_,idparametroref=idparametroref_).first()
        return jsonify(modelo.serialize())
    except Exception as e:
	      return(str(e))


if __name__ == '__main__':
    app.run()