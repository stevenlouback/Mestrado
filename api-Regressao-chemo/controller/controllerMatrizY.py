from sqlalchemy import func

from models.modelMatrizY import MatrizY

def geraMatrizY(db, objeto):
  idmodelo = objeto['idmodelo']
  idamostra = objeto['idamostra']
  idparametroref = objeto['idparametroref']
  idcalibracao = objeto['idcalibracao']
  vlresultado = objeto['vlresultado']
  vlreferencia = objeto['vlreferencia']
  dtpredicao = objeto['dtpredicao']

  # Pega a ultima sequencia para gravar no banco
  nrsequencia = (db.session.query(func.max(MatrizY.nrsequencia)).filter_by(idmodelo=idmodelo,
                                                                           idamostra=idamostra).scalar() or 0) + 1

  try:
    modelo = MatrizY(
      idmodelo=idmodelo,
      idamostra=idamostra,
      nrsequencia=nrsequencia,
      idparametroref=idparametroref,
      idcalibracao=idcalibracao,
      vlresultado=vlresultado,
      vlreferencia=vlreferencia,
      dtpredicao=dtpredicao
    )
    db.session.add(modelo)
    # db.session.commit()
    return "Matriz Y Registrada."
  except Exception as e:
    return (str(e))