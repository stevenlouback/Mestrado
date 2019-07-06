from sqlalchemy import func

from models.model import MatrizY
from datetime import datetime

def geraPredicao(db, objeto):
  print("Antes das Conversoes")

  idamostra = objeto['idamostra']
  print(idamostra)
  idmodelo = objeto['idmodelo']
  print(idmodelo)
  vlresultado = objeto['valorpredito']
  print(vlresultado)

  matrizy = MatrizY.query.filter_by(idmodelo=idmodelo, idamostra=idamostra).first()

  idparametroref = matrizy.idparametroref
  idcalibracao = matrizy.idcalibracao
  vlreferencia = matrizy.vlreferencia
  dtpredicao = str(datetime.now())

  try:
    print("entrando")
    matryy = MatrizY(
      idmodelo=idmodelo,
      idamostra=idamostra,
      idparametroref=idparametroref,
      idcalibracao=idcalibracao,
      vlresultado=vlresultado,
      vlreferencia=vlreferencia,
      dtpredicao=dtpredicao
    )

    print('merge: ', idmodelo)
    print('merge: ', idamostra)
    db.session.merge(matryy)

    return "Amostra Atualizada com sucesso o. idamostra={}".format(matryy.idamostra)
  except Exception as e:
    return (str(e))