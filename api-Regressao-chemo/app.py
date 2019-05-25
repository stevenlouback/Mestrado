from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import engine

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models.modelModeloCal import ModeloCalibracao

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/modelo/add")
def add_modelo():
    nmmodelo=request.args.get('nmmodelo')
    nmmetodoreferencia=request.args.get('nmmetodoreferencia')
    tpinstrumento=request.args.get('tpinstrumento')
    dsmodelo = request.args.get('dsmodelo')
    dtcriacao = request.args.get('dtcriacao')
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


if __name__ == '__main__':
    app.run()