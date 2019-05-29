from sqlalchemy import func

from models.modelModeloCal import ModeloCalibracao

def geraModelo(db, objeto):

  nmmodelo = objeto['nmmodelo']
  nmmetodoreferencia = objeto['nmmetodoreferencia']
  tpinstrumento = objeto['tpinstrumento']
  dsmodelo = objeto['dsmodelo']
  dtcriacao = objeto['dtcriacao']



  # Pega a ultima sequencia para gravar no banco
  idmodelo = (db.session.query(func.max(ModeloCalibracao.idmodelo)).scalar() or 0) + 1

  try:
    modelo = ModeloCalibracao(
      idmodelo=idmodelo,
      nmmodelo=nmmodelo,
      nmmetodoreferencia=nmmetodoreferencia,
      tpinstrumento=tpinstrumento,
      dsmodelo=dsmodelo,
      dtcriacao=dtcriacao
    )
    db.session.add(modelo)

    return "Modelo Adicionado. idmodelo={}".format(modelo.idmodelo)
  except Exception as e:
    return (str(e))