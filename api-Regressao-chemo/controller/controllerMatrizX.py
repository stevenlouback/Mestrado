from sqlalchemy import func

from models.model import MatrizX

def geraMatrizX(db, objeto):
  idmodelo = objeto['idmodelo']
  idamostra = objeto['idamostra']
  nrposicaolinha = objeto['nrposicaolinha']
  nrposicaocoluna = objeto['nrposicaocoluna']
  vllinhacoluna = objeto['vllinhacoluna']

  # Pega a ultima sequencia para gravar no banco
  nrsequencia = (db.session.query(func.max(MatrizX.nrsequencia)).filter_by(idmodelo=idmodelo,idamostra=idamostra).scalar() or 0) + 1

  try:
    modelo = MatrizX(
      idmodelo=idmodelo,
      idamostra=idamostra,
      nrsequencia=nrsequencia,
      nrposicaolinha=nrposicaolinha,
      nrposicaocoluna=nrposicaocoluna,
      vllinhacoluna=vllinhacoluna
    )
    db.session.add(modelo)
    # db.session.commit()
    return "Matriz X Registrada."
  except Exception as e:
    return (str(e))