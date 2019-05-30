from models.model import AmostraCalibracao


def geraAmostraCalibracao (db, objeto):
  idmodelo = objeto['idmodelo']
  idamostra = objeto['idamostra']
  idcalibracao = objeto['idcalibracao']

  try:
    modelo = AmostraCalibracao(
      idmodelo=idmodelo,
      idamostra=idamostra,
      idcalibracao=idcalibracao
    )
    db.session.add(modelo)
    # db.session.commit()
    return "Amostra da Calibração Adicionada."
  except Exception as e:
    return (str(e))