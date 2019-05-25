from app import db


class AmostraCalibracao(db.Model):
    __tablename__ = 'amostra_calibracao'

    idmodelo = db.Column(db.Integer, primary_key=True)
    idamostra = db.Column(db.Integer, primary_key=True)
    idcalibracao = db.Column(db.Integer, primary_key=True)

    def __init__(self, idmodelo, tpamostra, dsobservacoes, dtcoletaamostra):
        self.idmodelo = idmodelo
        self.tpamostra = tpamostra
        self.dsobservacoes = dsobservacoes
        self.dtcoletaamostra = dtcoletaamostra

    def __repr__(self):
        return {
            '<idmodelo {}>'.format(self.idmodelo),
            '<idamostra{}'.format(self.idamostra)
        }

    def serialize(self):
        return {
            'idmodelo': self.idmodelo,
            'idamostra': self.idamostra,
            'tpamostra': self.tpamostra,
            'dsobservacoes': self.dsobservacoes,
            'dtcoletaamostra': self.dtcoletaamostra
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
