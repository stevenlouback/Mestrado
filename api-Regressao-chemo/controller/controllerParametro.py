from sqlalchemy import func

from models.model import Parametro

def geraParametro(db, objeto):
  idmodelo = objeto['idmodelo']
  nmparametroref = objeto['nmparametroref']

  # Pega a ultima sequencia para gravar no banco
  idparametroref = (db.session.query(func.max(Parametro.idparametroref)).filter_by(
    idmodelo=idmodelo).scalar() or 0) + 1

  try:
    modelo = Parametro(
      idparametroref=idparametroref,
      idmodelo=idmodelo,
      nmparametroref=nmparametroref
    )
    db.session.add(modelo)
    db.session.commit()
    return "Parametros Registrado."
  except Exception as e:
    return (str(e))