from app import db


class MatrizY(db.Model):
    __tablename__ = 'matrizY'

    # idmodelo        = db.Column(db.Integer, db.ForeignKey('amostra.idmodelo'), db.ForeignKey('parametro.idmodelo'), primary_key=True)
    # idamostra       = db.Column(db.Integer, db.ForeignKey('amostra.idamostra'), primary_key=True)
    idmodelo = db.Column(db.Integer,primary_key=True)
    idamostra = db.Column(db.Integer, primary_key=True)
    idparametroref  = db.Column(db.Integer, primary_key=True)
    idcalibracao    = db.Column(db.Integer, nullable=False)
    vlresultado    = db.Column(db.Numeric, nullable=False)
    vlreferencia    = db.Column(db.Numeric, nullable=False)
    dtpredicao = db.Column(db.DateTime, nullable=False)


    def __init__(self, idmodelo,idamostra,nrsequencia,idparametroref,idcalibracao,vlresultado,vlreferencia,dtpredicao):
        self.idmodelo = idmodelo
        self.idamostra = idamostra
        self.nrsequencia = nrsequencia
        self.idparametroref = idparametroref
        self.idcalibracao = idcalibracao
        self.vlresultado = vlresultado
        self.vlreferencia = vlreferencia
        self.dtpredicao = dtpredicao

    def __repr__(self):
        return '<matrizY{}'.format(self.nrsequencia,self.idmodelo,self.idamostra)

    def serialize(self):
        return {
            'idmodelo': self.idmodelo,
            'idamostra': self.idamostra,
            'nrsequencia': self.nrsequencia,
            'idparametroref': self.idparametroref,
            'idcalibracao': self.idcalibracao,
            'vlresultado': self.vlresultado,
            'vlreferencia': self.vlreferencia,
            'dtpredicao': self.dtpredicao
        }