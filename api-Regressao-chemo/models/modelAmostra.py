from app import db

class Amostra(db.Model):
    __tablename__ = 'amostra'

    idmodelo = db.Column(db.Integer, db.ForeignKey('modelo.idmodelo'), primary_key=True)
    idamostra = db.Column(db.Integer, primary_key=True,autoincrement=True)
    tpamostra = db.Column(db.String(), nullable=False)
    dsobservacoes = db.Column(db.String(), nullable=True)
    dtcoletaamostra = db.Column(db.DateTime, nullable=False)

    # matrizesX = db.relationship('MatrizX', backref='Amostra', lazy=True)
    # matrizesY = db.relationship('MatrizY', backref='Amostra', lazy=True)
    # amostrascalibracao = db.relationship('AmostraCalibracao', backref='Amostra', lazy=True)

    def __init__(self, idmodelo,idamostra, tpamostra, dsobservacoes, dtcoletaamostra):
        self.idmodelo = idmodelo
        self.idamostra = idamostra
        self.tpamostra = tpamostra
        self.dsobservacoes = dsobservacoes
        self.dtcoletaamostra = dtcoletaamostra

    def __repr__(self):
        return "<Amostras(%s, %s)>" % (
            self.idmodelo, self.idamostra)

    def serialize(self):
        return {
            'idmodelo': self.idmodelo,
            'idamostra': self.idamostra,
            'tpamostra': self.tpamostra,
            'dsobservacoes': self.dsobservacoes,
            'dtcoletaamostra': self.dtcoletaamostra.strftime("%d/%m/%Y")
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            if key == 'password':
                self.password = self.__generate_hash(value)
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_amostra(idmodelo):
        return Amostra.query.get(idmodelo)

    @staticmethod
    def get_one_amostra(idmodelo,iddamostra):
        return Amostra.query.filter_by(idm=value).first()

    @staticmethod
    def get_user_by_email(value):
        return Amostra.query.filter_by(email=value).first()
