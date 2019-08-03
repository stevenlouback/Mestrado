from flask import jsonify
from sqlalchemy import func

from models.model import Amostra

def geraAmostra(db, objeto):
  idamostra =  objeto['idamostra']

  # RECUPERA O JSON DENTRO DE JSON
  modelo = objeto['modelo']
  idmodelo = modelo['idmodelo']

  idmodelo = idmodelo

  tpamostra = objeto['tpamostra']
  dsobservacoes = objeto['dsobservacoes']
  dtcoletaamostra = objeto['dtcoletaamostra']
  imamostra = objeto['imamostra']

  if not objeto['dsespectro']:
    print('passou')
  else:
    dsespectro= objeto['dsespectro']

  nmidentifica= objeto['nmidentifica']

  # Pega a ultima sequencia para gravar no banco

  # Pega a ultima sequencia para gravar no banco
  if idamostra == "":
    idamostra = (db.session.query(func.max(Amostra.idamostra)).filter_by(idmodelo=idmodelo).scalar() or 0) + 1

  if idamostra == 0:
    idamostra = (db.session.query(func.max(Amostra.idamostra)).filter_by(idmodelo=idmodelo).scalar() or 0) + 1

  try:
    modelo = Amostra(
      idmodelo=idmodelo,
      idamostra=idamostra,
      tpamostra=tpamostra,
      dsobservacoes=dsobservacoes,
      dtcoletaamostra=dtcoletaamostra,
      imamostra=imamostra,
      dsespectro=dsespectro,
      nmidentifica=nmidentifica
    )
    db.session.add(modelo)
    # db.session.commit()
    return modelo.idamostra
  except Exception as e:
    return (str(e))