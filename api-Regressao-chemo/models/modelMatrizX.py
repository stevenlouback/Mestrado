from app import db


class MatrizX(db.Model):
    __tablename__ = 'matrizX'

    # idmodelo        = db.Column(db.Integer, db.ForeignKey('Amostra.idmodelo'), primary_key=True)
    # idamostra       = db.Column(db.Integer, db.ForeignKey('Amostra.idamostra'), primary_key=True)
    idmodelo = db.Column(db.Integer, primary_key=True)
    idamostra = db.Column(db.Integer, primary_key=True)
    nrsequencia     = db.Column(db.Integer, primary_key=True)
    nrposicaolinha  = db.Column(db.Integer, nullable=False)
    nrposicaocoluna = db.Column(db.Integer, nullable=False)
    vllinhacoluna   = db.Column(db.Numeric, nullable=False)

    def __init__(self, idmodelo, idamostra, nrposicaolinha, nrposicaocoluna, vllinhacoluna):
        self.idmodelo = idmodelo
        self.idamostra = idamostra
        self.nrposicaolinha = nrposicaolinha
        self.nrposicaocoluna = nrposicaocoluna
        self.vllinhacoluna = vllinhacoluna

    def __repr__(self):
        return '<matrizX{}'.format(self.nrsequencia,self.idmodelo,self.idamostra)

    def serialize(self):
        return {
            'idmodelo': self.idmodelo,
            'idamostra': self.idamostra,
            'nrsequencia': self.nrsequencia,
            'nrposicaolinha': self.nrposicaolinha,
            'nrposicaocoluna': self.nrposicaocoluna,
            'vllinhacoluna': self.vllinhacoluna
        }