from sqlalchemy.ext.orderinglist import ordering_list

from app import db


class ModeloCalibracao(db.Model):
    __tablename__ = 'modelo'

    idmodelo = db.Column(db.Integer, primary_key=True)
    nmmodelo = db.Column(db.String(), unique=True, nullable=False)
    nmmetodoreferencia = db.Column(db.String(), nullable=False)
    tpinstrumento = db.Column(db.String(), nullable=False)
    dsmodelo = db.Column(db.String(), nullable=True)
    dtcriacao = db.Column(db.DateTime, nullable=False)

    amostra   = db.relationship('Amostra', cascade='all,delete', backref='ModeloCalibracao', lazy=True, uselist=True,
        collection_class=ordering_list("idamostra", count_from=1))
    parametros = db.relationship('Parametro', cascade='all,delete', backref='ModeloCalibracao', lazy=True, uselist=True,
        collection_class=ordering_list("idparametroref", count_from=1))

    def __init__(self, idmodelo, nmmodelo, nmmetodoreferencia, tpinstrumento, dsmodelo, dtcriacao):
        self.idmodelo = idmodelo
        self.nmmodelo = nmmodelo
        self.nmmetodoreferencia = nmmetodoreferencia
        self.tpinstrumento = tpinstrumento
        self.dsmodelo = dsmodelo
        self.dtcriacao = dtcriacao

    def __repr__(self):
        return '<idmodelo {}>'.format(self.idmodelo)

    def serialize(self):

        return {
            'idmodelo': self.idmodelo,
            'nmmodelo': self.nmmodelo,
            'nmmetodoreferencia': self.nmmetodoreferencia,
            'tpinstrumento': self.tpinstrumento,
            'dsmodelo': self.dsmodelo,
            'dtcriacao': self.dtcriacao.strftime("%d/%m/%Y")
        }