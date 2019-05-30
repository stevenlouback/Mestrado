from sqlalchemy import func

from models.model import Calibracao

def geraCalibracao(db, objeto):
  idmodelo = objeto['idmodelo']
  inativo = objeto['inativo']
  dtcalibracao = objeto['dtcalibracao']

  try:
    modelo = Calibracao(
      idmodelo=idmodelo,
      inativo=inativo,
      dtcalibracao=dtcalibracao
    )
    db.session.add(modelo)
    # db.session.commit()
    return "Calibração Registrada."
  except Exception as e:
    return (str(e))