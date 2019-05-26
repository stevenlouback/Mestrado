from app import db


class AmostraCalibracao(db.Model):
    __tablename__ = 'amostra_calibracao'

    # idmodelo = db.Column(db.Integer, db.ForeignKey('amostra.idmodelo'), primary_key=True)
    # idamostra = db.Column(db.Integer, db.ForeignKey('amostra.idamostra'), primary_key=True)
    # idcalibracao = db.Column(db.Integer, db.ForeignKey('calibracao.idcalibracao'), primary_key=True)
    idmodelo = db.Column(db.Integer, primary_key=True)
    idamostra = db.Column(db.Integer, primary_key=True)
    idcalibracao = db.Column(db.Integer, primary_key=True)

    def __init__(self, idmodelo, idamostra, idcalibracao):
        self.idmodelo = idmodelo
        self.idamostra = idamostra
        self.idcalibracao = idcalibracao

    def __repr__(self):
        return {
            '<idmodelo {}>'.format(self.idmodelo),
            '<idamostra{}'.format(self.idamostra),
            '<idcalibracao{}'.format(self.idcalibracao)
        }

    def serialize(self):
        return {
            'idmodelo': self.idmodelo,
            'idamostra': self.idamostra,
            'idcalibracao': self.idcalibracao
        }