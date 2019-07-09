from sqlalchemy import func

from models.model import ModeloCalibracao

def geraModelo(db, objeto):
  nmmodelo = objeto['nmmodelo']
  nmmetodoreferencia = objeto['nmmetodoreferencia']
  tpinstrumento = objeto['tpinstrumento']
  dsmodelo = objeto['dsmodelo']
  dtcriacao = objeto['dtcriacao']
  idmodelo = objeto['idmodelo']

  # Pega a ultima sequencia para gravar no banco
  if idmodelo == "":
    idmodelo = (db.session.query(func.max(ModeloCalibracao.idmodelo)).scalar() or 0) + 1

  if idmodelo == 0:
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
    if idmodelo == "":
      db.session.add(modelo)
    else:
      print('merge: ', idmodelo)
      db.session.merge(modelo)

    return "Modelo Adicionado. idmodelo={}".format(modelo.idmodelo)
  except Exception as e:
    return (str(e))