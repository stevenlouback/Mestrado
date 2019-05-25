from app import db


class ModeloCalibracao(db.Model):
    __tablename__ = 'modelo'

    idmodelo        = db.Column(db.Integer, primary_key=True)
    idamostra       = db.Column(db.Integer, primary_key=True)
    nrsequencia     = db.Column(db.Integer, primary_key=True)
    nrposicaolinha  = db.Column(db.Integer, required=True)
    nrposicaocoluna = db.Column(db.Integer, required=True)
    vllinhacoluna   = db.Column(db.Numeric, required=True)

    def __init__(self, nmmodelo, nmmetodoreferencia, tpinstrumento, dsmodelo, dtcriacao):
        self.nmmodelo = nmmodelo
        self.nmmetodoreferencia = nmmetodoreferencia
        self.tpinstrumento = tpinstrumento
        self.dsmodelo = dsmodelo
        self.dtcriacao = dtcriacao

    def __repr__(self):
        return '<id {}>'.format(self.idmodelo)

    def serialize(self):
        return {
            'idmodelo': self.idmodelo,
            'nmmodelo': self.nmmodelo,
            'nmmetodoreferencia': self.nmmetodoreferencia,
            'tpinstrumento': self.tpinstrumento,
            'dsmodelo': self.dsmodelo,
            'dtcriacao': self.dtcriacao
        }