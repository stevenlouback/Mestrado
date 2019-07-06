from sqlalchemy.ext.orderinglist import ordering_list

from app import db

##################################################################
#Modelo Amostra
##################################################################
class Amostra(db.Model):
###########################################################
    __tablename__ = 'amostra'

    idmodelo = db.Column(db.Integer, primary_key=True)
    idamostra = db.Column(db.Integer, primary_key=True,autoincrement=True)
    tpamostra = db.Column(db.String(), nullable=False)
    dsobservacoes = db.Column(db.String(), nullable=True)
    dtcoletaamostra = db.Column(db.DateTime, nullable=False)
    imamostra = db.Column(db.String(), nullable=True)

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




#########################################################################
class AmostraCalibracao(db.Model):
###########################################################
    __tablename__ = 'amostra_calibracao'

    # idmodelo = db.Column(db.Integer, db.ForeignKey(Amostra.idmodelo), primary_key=True)
    # idamostra = db.Column(db.Integer, db.ForeignKey(Amostra.idamostra), primary_key=True)
    # idcalibracao = db.Column(db.Integer, db.ForeignKey(Calibracao.idcalibracao), primary_key=True)
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


#########################################################
class Calibracao(db.Model):
###########################################################
    __tablename__ = 'calibracao'

    idmodelo = db.Column(db.Integer, primary_key=True)
    idcalibracao = db.Column(db.Integer, primary_key=True)
    inativo = db.Column(db.String(), nullable=True)
    dtcalibracao = db.Column(db.DateTime, nullable=False)

    # amostra_calibracao = db.relationship(AmostraCalibracao, backref=Calibracao, lazy=True)

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
            'dtcoletaamostra': self.dtcoletaamostra.strftime("%d/%m/%Y")
        }



#####################################################
class MatrizX(db.Model):
###########################################################
    __tablename__ = 'matrizX'

    idmodelo = db.Column(db.Integer, primary_key=True)
    idamostra = db.Column(db.Integer, primary_key=True)
    nrsequencia = db.Column(db.Integer, primary_key=True)
    nrposicaolinha = db.Column(db.Integer, nullable=False)
    nrposicaocoluna = db.Column(db.Integer, nullable=False)
    vllinhacoluna = db.Column(db.Numeric, nullable=False)

    def __init__(self, idmodelo, idamostra, nrsequencia, nrposicaolinha, nrposicaocoluna, vllinhacoluna):
        self.idmodelo = idmodelo
        self.idamostra = idamostra
        self.nrsequencia = nrsequencia
        self.nrposicaolinha = nrposicaolinha
        self.nrposicaocoluna = nrposicaocoluna
        self.vllinhacoluna = vllinhacoluna

    def __repr__(self):
        return '<matrizX{}'.format(self.nrsequencia, self.idmodelo, self.idamostra)

    def serialize(self):
        return {
            'idmodelo': self.idmodelo,
            'idamostra': self.idamostra,
            'nrsequencia': self.nrsequencia,
            'nrposicaolinha': self.nrposicaolinha,
            'nrposicaocoluna': self.nrposicaocoluna,
            'vllinhacoluna': self.vllinhacoluna
        }

###########################################################
class MatrizY(db.Model):
###########################################################
    __tablename__ = 'matrizY'

    # idmodelo        = db.Column(db.Integer, db.ForeignKey(Amostra.idmodelo), db.ForeignKey(Parametro.idmodelo), primary_key=True)
    # idamostra       = db.Column(db.Integer, db.ForeignKey(Amostra.idamostra), primary_key=True)
    idmodelo = db.Column(db.Integer, primary_key=True)
    idamostra = db.Column(db.Integer, primary_key=True)
    idparametroref = db.Column(db.Integer, primary_key=True)
    idcalibracao = db.Column(db.Integer, nullable=True)
    vlresultado = db.Column(db.Numeric, nullable=True)
    vlreferencia = db.Column(db.Numeric, nullable=True)
    dtpredicao = db.Column(db.DateTime, nullable=True)

    def __init__(self, idmodelo, idamostra, nrsequencia, idparametroref, idcalibracao, vlresultado, vlreferencia,
                 dtpredicao):
        self.idmodelo = idmodelo
        self.idamostra = idamostra
        self.nrsequencia = nrsequencia
        self.idparametroref = idparametroref
        self.idcalibracao = idcalibracao
        self.vlresultado = vlresultado
        self.vlreferencia = vlreferencia
        self.dtpredicao = dtpredicao

    def __repr__(self):
        return '<matrizY{}'.format(self.nrsequencia, self.idmodelo, self.idamostra)

    def serialize(self):
        return {
            'idmodelo': self.idmodelo,
            'idamostra': self.idamostra,
            'nrsequencia': self.nrsequencia,
            'idparametroref': self.idparametroref,
            'idcalibracao': self.idcalibracao,
            'vlresultado': self.vlresultado,
            'vlreferencia': self.vlreferencia,
            'dtpredicao': self.dtpredicao.strftime("%d/%m/%Y")
        }

#######################################################################
class ModeloCalibracao(db.Model):
#######################################################################
    __tablename__ = 'modelo'

    idmodelo = db.Column(db.Integer, primary_key=True)
    nmmodelo = db.Column(db.String(), unique=True, nullable=False)
    nmmetodoreferencia = db.Column(db.String(), nullable=False)
    tpinstrumento = db.Column(db.String(), nullable=False)
    dsmodelo = db.Column(db.String(), nullable=True)
    dtcriacao = db.Column(db.DateTime, nullable=False)

    # amostra   = db.relationship('Amostra', cascade='all,delete', backref='ModeloCalibracao', lazy=True, uselist=True,
    #     collection_class=ordering_list("idamostra", count_from=1))
    # parametros = db.relationship('Parametro', cascade='all,delete', backref='ModeloCalibracao', lazy=True, uselist=True,
    #     collection_class=ordering_list("idparametroref", count_from=1))

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

######################################################
class Parametro(db.Model):
######################################################
    __tablename__ = 'parametro'

    idmodelo = db.Column(db.Integer, primary_key=True)
    idparametroref = db.Column(db.Integer, primary_key=True)
    nmparametroref = db.Column(db.String(), nullable=False)

    # matrizesY = db.relationship('MatrizY', backref='Parametro', lazy=True)

    def __init__(self, idparametroref, idmodelo, nmparametroref):
      self.idparametroref = idparametroref
      self.idmodelo = idmodelo
      self.nmparametroref = nmparametroref

    def __repr__(self):
      return {
          '<Parametro {}>'.format(self.idmodelo, self.idparametroref)
      }

    def serialize(self):
      return {
          'idmodelo': self.idmodelo,
          'idparametroref': self.idparametroref,
          'nmparametroref': self.nmparametroref
      }
