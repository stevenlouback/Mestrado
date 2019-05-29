from sqlalchemy import func

from models.modelAmostra import Amostra

def geraAmostra(db, objeto):
  idmodelo = objeto['idmodelo']
  tpamostra = objeto['tpamostra']
  dsobservacoes = objeto['dsobservacoes']
  dtcoletaamostra = objeto['dtcoletaamostra']

  # Pega a ultima sequencia para gravar no banco
  idamostra = (db.session.query(func.max(Amostra.idamostra)).filter_by(idmodelo=idmodelo).scalar() or 0) + 1

  try:
    modelo = Amostra(
      idmodelo=idmodelo,
      idamostra=idamostra,
      tpamostra=tpamostra,
      dsobservacoes=dsobservacoes,
      dtcoletaamostra=dtcoletaamostra
    )
    db.session.add(modelo)
    # db.session.commit()
    return "Amostra Adicionada. idmodelo={}".format(modelo.idmodelo) + " idAmostra={}".format(modelo.idamostra)
  except Exception as e:
    return (str(e))