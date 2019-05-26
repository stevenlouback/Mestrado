import uuid

from app import db


class Parametro(db.Model):
    __tablename__ = 'parametro'

    idmodelo = db.Column(db.Integer, db.ForeignKey('modelo.idmodelo'), primary_key=True)
    idparametroref = db.Column(db.Integer, primary_key=True)
    nmparametroref = db.Column(db.String(), unique=True, nullable=False)

    # matrizesY = db.relationship('MatrizY', backref='Parametro', lazy=True)

    def __init__(self, idparametroref,idmodelo, nmparametroref):
        self.idparametroref = idparametroref
        self.idmodelo = idmodelo
        self.nmparametroref = nmparametroref

    def __repr__(self):
        return {
            '<Parametro {}>'.format(self.idmodelo,self.idparametroref)
        }

    def serialize(self):
        return {
            'idmodelo': self.idmodelo,
            'nmmodelo': self.nmmodelo,
            'nmmetodoreferencia': self.nmmetodoreferencia,
            'tpinstrumento': self.tpinstrumento,
            'dsmodelo': self.dsmodelo,
            'dtcriacao': self.dtcriacao
        }