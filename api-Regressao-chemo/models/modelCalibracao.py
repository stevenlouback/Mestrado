from app import db


class Calibracao(db.Model):
    __tablename__ = 'calibracao'

    idmodelo = db.Column(db.Integer, primary_key=True)
    idcalibracao = db.Column(db.Integer, primary_key=True)
    inativo = db.Column(db.String(), nullable=True)
    dtcalibracao = db.Column(db.DateTime, nullable=False)

    # amostra_calibracao = db.relationship('amostra_calibracao', backref='Calibracao', lazy=True)

    def __init__(self, idmodelo, inativo, dtcalibracao):
        self.idmodelo = idmodelo
        self.inativo = inativo
        self.dtcalibracao = dtcalibracao

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
