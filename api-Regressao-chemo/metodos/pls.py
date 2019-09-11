import sys
import numpy as np
# import matplotlib.pyplot as plt
import json
from math import sqrt
from flask import jsonify
from datetime import datetime
from scipy import stats
from pyod.models.knn import KNN
# from sksos import SOS
from metodos.pca import PCA

sys.path.append("..\dao")

from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import r2_score, mean_squared_error, median_absolute_error, mean_absolute_error, \
  mean_squared_log_error, coverage_error, label_ranking_loss, explained_variance_score, \
  label_ranking_average_precision_score
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from sklearn import metrics

from sqlalchemy import create_engine

db_string = "postgresql://postgres:postgres@localhost:5432/Quimiometria"
# db_string = "postgresql://postgres:postgres@localhost:5432/bkpSteven"

db = create_engine(db_string)

Session = sessionmaker(bind=db)
session = Session()


class PLS(object):

  def predicao(self, idmodelo, idamostra):

    idmodelo = idmodelo

    idamostra = idamostra

    print(idmodelo)
    print(idamostra)

    X = self.selectMatrizX(idmodelo, "VALIDACAO")
    Y = self.selectMatrizY(idmodelo, "VALOR", "VALIDACAO")

    amostraPredicao = self.selectAmostra(idamostra, idmodelo)

    valorReferencia = self.selectDadosReferenciaAmostra(idamostra, idmodelo)

    pls = PLSRegression(copy=True, max_iter=500, n_components=20, scale=False, tol=1e-06)

    pls.fit(X, Y)
    print(amostraPredicao)
    valorPredito = pls.predict(amostraPredicao)

    print('Amostra: ' + str(idamostra) + ' - Valor Predito :' + str(valorPredito) + ' - Valor Referencia :' + str(
      valorReferencia))

    cursorDadosCalibracao = db.execute("select rmsec, rmsep, coeficientecal, coeficienteval, dtcalibracao "
                                       "from calibracao where inativo = 'A' and idmodelo = " + str(idmodelo) + " ")
    for regCodigo in cursorDadosCalibracao:
      rmsec = regCodigo[0]
      rmsep = regCodigo[1]
      coeficienteCal = regCodigo[2]
      coeficienteVal = regCodigo[3]
      dtcalibracao = regCodigo[4]

    print(rmsec)
    print(rmsep)
    print(coeficienteCal)
    print(coeficienteVal)
    print(dtcalibracao)

    dtcalibracao = dtcalibracao.strftime('%d/%m/%Y')
    print(dtcalibracao)

    # tratamento dos dados para o Json
    coeficienteCal = round(coeficienteCal, 2)
    coeficienteVal = round(coeficienteVal, 2)
    rmsec = round(rmsec, 2)
    rmsep = round(rmsep, 2)
    valorReferencia = round(valorReferencia, 2)

    valorPreditoString = str(valorPredito)
    valorPreditoString = valorPreditoString.replace("[", "")
    valorPreditoString = valorPreditoString.replace("]", "")

    ##Contrucao do JSON
    json_data = jsonify(idamostra=str(idamostra), valorpredito=str(valorPreditoString),
                        rmsec=str(rmsec), rmsep=str(rmsep), idmodelo=str(idmodelo), dtcalibracao=str(dtcalibracao),
                        valorreferencia=str(valorReferencia), coeficientecal=str(coeficienteCal), coeficienteval=str(coeficienteVal))

    return json_data

  def selectAmostra(self, idAmostra, idmodelo):

    try:
      # numero de colunas da matriz
      cursorColunas = db.execute("select max(x.nrposicaocoluna) from matrizx x where x.idamostra = " + str(
        idAmostra) + "  and x.idmodelo = " + str(idmodelo) + "")

      contadorColunas = 0

      for linha in cursorColunas:
        contadorColunas = linha[0]

      # Preenchimento da MatrizX
      matrizX = []

      cursorAmostras = db.execute("select x.idamostra from matrizx x "
                                  "where x.idamostra =  " + str(idAmostra) + ""
                                                                             "  and x.idmodelo = " + str(idmodelo) + ""
                                                                                                                     " group by x.idamostra order by x.idamostra asc")

      listaAmostras = []
      for regAmostras in cursorAmostras:
        listaAmostras.append(regAmostras[0])

      # print(listaAmostras)

      for amostra in listaAmostras:
        # print(amostra)
        linhaMatriz = []

        cursorDadosAmostra = db.execute("SELECT x.idamostra, x.vllinhacoluna FROM matrizx x "
                                        "where x.idamostra = " + str(amostra) + ""
                                                                                "  and x.idmodelo = " + str(
          idmodelo) + ""
                      " order by x.idamostra, x.nrsequencia, x.nrposicaolinha, x.nrposicaocoluna asc")

        for regDadosAmostra in cursorDadosAmostra:
          if regDadosAmostra[1] == 0E-8:
            linhaMatriz.append('0')
          else:
            linhaMatriz.append(regDadosAmostra[1])
            # x=Symbol('x')
            # difx = diff(regDadosAmostra[1], x)
            # linhaMatriz.append(difx)

        # print(amostra)
        # print(linhaMatriz)
        matrizX += [linhaMatriz]

      # print('AMOSTRA SELECIONADA')
      # print(matrizX)

      return matrizX
    except Exception:
      # print(Exception)
      return "Ocorreu um erro na busca dos dados"

  def selectMatrizX(self, idModelo, conjunto):

    try:
      # numero de colunas da matriz

      if conjunto == "TODOS":
        sqlConsulta = (" inner join matrizy y on (x.idamostra = y.idamostra and y.idmodelo = x.idmodelo) "
                       " inner join amostra a on ( a.idamostra = x.idamostra and a.idmodelo = x.idmodelo ) ")
        whereConsulta = ("where x.idModelo = " + str(idModelo) + "  and a.tpamostra <> 'OUTLIER' ")

      elif conjunto == "CALIBRAR":
        sqlConsulta = (" inner join matrizy y on (x.idamostra = y.idamostra and y.idmodelo = x.idmodelo) "
                       "inner join amostra a on ( a.idamostra = x.idamostra and a.idmodelo = x.idmodelo ) "
                       "inner join amostra_calibracao ac on ( a.idamostra = ac.idamostra and a.idmodelo = ac.idmodelo ) "
                       "inner join calibracao c on ( c.idcalibracao = ac.idcalibracao and c.inativo = 'A' ) ")
        whereConsulta = ("where x.idModelo = " + str(
          idModelo) + " and ac.tpconjunto = 'NORMAL'  and a.tpamostra <> 'OUTLIER' ")

      elif conjunto == "CALIBRACAO":
        sqlConsulta = (" inner join matrizy y on (x.idamostra = y.idamostra and y.idmodelo = x.idmodelo) "
                       "inner join amostra a on ( a.idamostra = x.idamostra and a.idmodelo = x.idmodelo ) "
                       "inner join amostra_calibracao ac on ( a.idamostra = ac.idamostra and a.idmodelo = ac.idmodelo ) "
                       "inner join calibracao c on ( c.idcalibracao = ac.idcalibracao and c.inativo = 'A' ) ")
        whereConsulta = ("where x.idModelo = " + str(
          idModelo) + " and ac.tpconjunto = 'CALIBRACAO'  and a.tpamostra <> 'OUTLIER' ")

      elif conjunto == "VALIDACAO":
        sqlConsulta = (" inner join matrizy y on (x.idamostra = y.idamostra and y.idmodelo = x.idmodelo) "
                       "inner join amostra a on ( a.idamostra = x.idamostra and a.idmodelo = x.idmodelo ) "
                       "inner join amostra_calibracao ac on ( a.idamostra = ac.idamostra and a.idmodelo = ac.idmodelo ) "
                       "inner join calibracao c on ( c.idcalibracao = ac.idcalibracao and c.inativo = 'A' ) ")
        whereConsulta = (
              "where x.idModelo = " + str(idModelo) + " and ac.tpconjunto = 'VALIDACAO'  and a.tpamostra <> 'OUTLIER' ")

      sqlColunas = (
            " select max(x.nrposicaocoluna) from matrizx x " + str(sqlConsulta) + " " + str(whereConsulta) + " ")
      cursorColunas = db.execute(sqlColunas)

      contadorColunas = 0

      for linha in cursorColunas:
        contadorColunas = linha[0]
        print(contadorColunas)

      # Preenchimento da MatrizX
      matrizX = []

      sqlListaAmostras = ("select x.idamostra from matrizx x  " + str(sqlConsulta) + str(
        whereConsulta) + "group by x.idamostra order by x.idamostra asc")
      cursorAmostras = db.execute(sqlListaAmostras)

      """cursorAmostras = db.execute("select x.idamostra from matrizx x  "
                                        "inner join matrizy y on (y.idamostra = x.idamostra and y.idmodelo = x.idmodelo) "
                                        "inner join amostra a on ( a.idamostra = x.idamostra and a.idmodelo = x.idmodelo ) "
                                        "where x.idModelo = " + str(idModelo) + "  "                                                                                  
                                        "group by x.idamostra order by x.idamostra asc")"""

      cont = 0
      listaAmostras = []
      for regAmostras in cursorAmostras:
        listaAmostras.append(regAmostras[0])
        cont = cont + 1

      print('...............................')
      print('Qtde de Amostras - Matriz X')
      print(conjunto)
      print(cont)
      print('...............................')

      for amostra in listaAmostras:
        # print(amostra)
        linhaMatriz = []

        cursorDadosAmostra = db.execute("SELECT idamostra, vllinhacoluna 	FROM matrizx x "
                                        "where x.idamostra = " + str(amostra) + " and x.idModelo = " + str(
          idModelo) + ""
                      "order by x.idamostra, x.nrsequencia, x.nrposicaolinha, x.nrposicaocoluna asc")

        for regDadosAmostra in cursorDadosAmostra:
          if regDadosAmostra[1] == 0E-8:
            linhaMatriz.append('0')
          else:
            linhaMatriz.append(regDadosAmostra[1])
            # x=Symbol('x')
            # difx = diff(regDadosAmostra[1], x)
            # linhaMatriz.append(difx)

        # print(amostra)
        # print(linhaMatriz)
        matrizX += [linhaMatriz]

      # print('MATRIZ - X')
      # print(matrizX)

      return matrizX
    except Exception:
      print(Exception)
      return "Ocorreu um erro na busca dos dados"

  def selectMatrizY(self, idmodelo, tipo, conjunto):

    try:
      if conjunto == "TODOS":
        sqlConsulta = (" select y.idamostra from matrizy y "
                       "inner join amostra a on (a.idamostra = y.idamostra and a.idmodelo = y.idmodelo) ")
        whereConsulta = (" where y.idmodelo = " + str(idmodelo) + " and a.tpamostra <> 'OUTLIER' ")

      elif conjunto == "CALIBRACAO":
        sqlConsulta = (" select ac.idamostra from amostra_calibracao ac "
                       " inner join amostra a on ( a.idamostra = ac.idamostra and a.idmodelo = ac.idmodelo ) "
                       " inner join calibracao c on ( c.idcalibracao = ac.idcalibracao and c.inativo = 'A' ) ")
        whereConsulta = (" where ac.idModelo = " + str(
          idmodelo) + " and ac.tpconjunto = 'CALIBRACAO'  and a.tpamostra <> 'OUTLIER' ")

      elif conjunto == "VALIDACAO":
        sqlConsulta = (" select ac.idamostra from amostra_calibracao ac "
                       " inner join amostra a on ( a.idamostra = ac.idamostra and a.idmodelo = ac.idmodelo ) "
                       " inner join calibracao c on ( c.idcalibracao = ac.idcalibracao and c.inativo = 'A' ) ")
        whereConsulta = (" where ac.idModelo = " + str(
          idmodelo) + " and ac.tpconjunto = 'VALIDACAO'  and a.tpamostra <> 'OUTLIER' ")

      matrizY = []

      sqlListaAmostras = (" " + str(sqlConsulta) + " " + str(whereConsulta) + " order by 1 asc")
      cursorAmostras = db.execute(sqlListaAmostras)

      """cursorAmostras = db.execute("select y.idamostra from matrizy y "
                                        "inner join amostra a on (a.idamostra = y.idamostra and a.idmodelo = y.idmodelo) "
                                        " where y.idmodelo = " + str(idmodelo) + " "                                                                                              
                                        "order by y.idamostra asc")"""

      listaAmostras = []
      cont = 0
      for regAmostras in cursorAmostras:
        listaAmostras.append(regAmostras[0])
        cont = cont + 1

      # print(listaAmostras)
      print('............................................')
      print('Qtde de Amostras - Matriz Y')
      print(conjunto)
      print(cont)
      print('............................................')

      for amostra in listaAmostras:
        # print(amostra)
        linhaMatriz = []

        cursorDadosAmostra = db.execute("select y.idamostra, y.vlreferencia from matrizy y "
                                        " where y.idamostra = " + str(amostra) + " "
                                                                                 " and y.idmodelo = " + str(
          idmodelo) + " "
                      " order by y.idamostra asc")

        for regDadosAmostra in cursorDadosAmostra:
          if regDadosAmostra[1] == 0E-8:
            linhaMatriz.append('0')
          else:
            if tipo == "ID":
              linhaMatriz.append(regDadosAmostra[0])
            if tipo == "VALOR":
              linhaMatriz.append(np.double(regDadosAmostra[1]))

        # print(amostra)
        # print(linhaMatriz)
        matrizY += [linhaMatriz]

      # print('MATRIZ - Y')
      # print(matrizY)

      return matrizY
    except Exception:
      print(Exception)
      return "Ocorreu um erro na busca dos dados"

  def selectDadosReferenciaAmostra(self, idAmostra, idmodelo):

    try:
      cursorDadosAmostra = db.execute(
        "SELECT y.vlreferencia FROM matrizy y where y.idamostra = " + str(idAmostra) + "  and y.idmodelo =  " + str(
          idmodelo) + "")

      for regDadosAmostra in cursorDadosAmostra:
        valorReferencia = regDadosAmostra[0]

      return valorReferencia
    except Exception:
      return "Ocorreu um erro na busca dos dados"

  def detectarOutlierKNN(self, idmodelo, Xtodos, corteOutlier):
    # Detecao Outliers 1--------------------------------------------------------------
    clf = KNN()
    clf.fit(Xtodos)

    # get outlier scores
    y_train_scores = clf.decision_scores_  # raw outlier scores
    y_test_scores = clf.decision_function(Xtodos)  # outlier scores

    YCodigoTodosComOutilier = self.selectMatrizY(idmodelo, "ID", "TODOS")

    cont = 0
    amostrasRemovidas = 0

    for itemOutilier in y_train_scores:
      if itemOutilier > corteOutlier:
        contTodos = 0
        for item in YCodigoTodosComOutilier:
          amostra = str(item)
          amostra = amostra.replace("[", "")
          amostra = amostra.replace("]", "")
          if contTodos == cont:
            db.execute(
              " update amostra set tpamostra = 'OUTLIER' where idamostra = " + str(amostra) + " and idmodelo = " + str(
                idmodelo) + "")
            print(itemOutilier)
            amostrasRemovidas = amostrasRemovidas + 1
            break
          contTodos = contTodos + 1
      cont = cont + 1

    session.commit()
    print("Numero de Amostras Removidas: " + str(amostrasRemovidas))
    return cont

  def outliersZScore(self, idmodelo, Xtodos, corteOutlier):
    y_train_scores = np.abs(stats.zscore(Xtodos))

    YCodigoTodosComOutilier = self.selectMatrizY(idmodelo, "ID", "TODOS")

    cont = 0
    amostrasRemovidas = 0

    for itemOutilier in y_train_scores:
      print(itemOutilier)
      if itemOutilier > corteOutlier:
        contTodos = 0
        for item in YCodigoTodosComOutilier:
          amostra = str(item)
          amostra = amostra.replace("[", "")
          amostra = amostra.replace("]", "")
          if contTodos == cont:
            db.execute(
              " update amostra set tpamostra = 'OUTLIER' where idamostra = " + str(amostra) + " and idmodelo = " + str(
                idmodelo) + "")
            print(itemOutilier)
            amostrasRemovidas = amostrasRemovidas + 1
            break
          contTodos = contTodos + 1
      cont = cont + 1

    session.commit()
    print("Numero de Amostras Removidas: " + str(amostrasRemovidas))
    return cont

  def calibracao(self, idmodelo, nrcomponentes, corteOutlier, qtdeRemocoes, executaPCA, qtdePC):

    # Inativa calibracoes anteriores
    db.execute(" update calibracao set  inativo = 'F'" +
               " where idmodelo = " + str(idmodelo) + " ")
    db.execute(" update amostra set tpamostra = 'NORMAL' where idmodelo = " + str(idmodelo) + "")
    session.commit()

    # cria calibracao para o modelo
    data_Atual = datetime.today()
    data_em_texto = data_Atual.strftime('%d/%m/%Y')

    cursorCodigo = db.execute(
      "select coalesce(max(idcalibracao),0) + 1 as codigo from calibracao where idmodelo = " + str(idmodelo) + " ")
    for regCodigo in cursorCodigo:
      idcalibracao = regCodigo[0]

    db.execute("insert into calibracao (idcalibracao, idmodelo, dtcalibracao, inativo) "
               "values (" + str(idcalibracao) + "," + str(idmodelo) + " , '" + str(data_em_texto) + "', 'A' )")
    session.commit()

    idmodelo = idmodelo

    print(idmodelo)

    Xtodos = self.selectMatrizX(idmodelo, "TODOS")

    # caso seja necessario PCA
    pca = PCA()
    if executaPCA == 'S':
      Xtodos = pca.testePCA(Xtodos,qtdePC)


    # ***************************************************************************************************************
    # inicio kennard-stone
    # data = pd.DataFrame(Xtodos)

    #Xtodos = self.selectMatrizX(idmodelo, "TODOS")
    number_of_samples = Xtodos.__len__()
    number_of_samples = number_of_samples * 0.65

    # selected_sample_numbers, remaining_sample_numbers = kennardstonealgorithm(X, number_of_samples)
    amostras_Calibracao = kennardStone(Xtodos, number_of_samples)

    # amostras_Calibracao = kennardStone(autoscaled_X, number_of_samples)
    print("amostras_Calibracao")
    print(amostras_Calibracao)
    print("---")
    print("remaining sample numbers")
    # print(remaining_sample_numbers)

    # Insercao das amostras de Validacao
    YCodigoTodos = self.selectMatrizY(idmodelo, "ID", "TODOS")

    for amostraX in YCodigoTodos:
      amostra = str(amostraX)
      amostra = amostra.replace("[", "")
      amostra = amostra.replace("]", "")
      db.execute("insert into amostra_calibracao (idcalibracao, idmodelo, idamostra, tpconjunto) "
                 "values (" + str(idcalibracao) + "," + str(idmodelo) + " , '" + str(
        int(float(amostra))) + "','VALIDACAO' )")

    session.commit()

    # Insercao das amostras de Calibracao
    cont = 0
    for amostraCalibracao in amostras_Calibracao:
      amostra = str(amostraCalibracao)
      amostra = amostra.replace("[", "")
      amostra = amostra.replace("]", "")
      db.execute("update  amostra_calibracao set tpconjunto = 'CALIBRACAO'  "
                 " where idcalibracao =" + str(idcalibracao) + " and idmodelo = " + str(idmodelo) +
                 " and idamostra = " + str(int(float(amostra))))
      session.commit()

      print(cont)
      cont = cont + 1
    session.commit()

    Xcal = self.selectMatrizX(idmodelo, "CALIBRACAO")
    Xval = self.selectMatrizX(idmodelo, "VALIDACAO")

    if executaPCA == 'S':
      Xcal = pca.testePCA(Xcal,qtdePC)
      Xval = pca.testePCA(Xval, qtdePC)

    qtde = 0
    if corteOutlier > 0:
      while qtde < qtdeRemocoes:
        self.detectarOutlierKNN(idmodelo, Xval, corteOutlier)
        self.detectarOutlierKNN(idmodelo, Xcal, corteOutlier)

        Xval = self.selectMatrizX(idmodelo, "VALIDACAO")
        Xcal = self.selectMatrizX(idmodelo, "CALIBRACAO")

        if executaPCA == 'S':
          Xcal = pca.testePCA(Xcal, qtdePC)
          Xval = pca.testePCA(Xval, qtdePC)

        qtde = qtde + 1

    Ycal = self.selectMatrizY(idmodelo, "VALOR", "CALIBRACAO")
    Yval = self.selectMatrizY(idmodelo, "VALOR", "VALIDACAO")

    YCodigoCal = self.selectMatrizY(idmodelo, "ID", "CALIBRACAO")
    YCodigoVal = self.selectMatrizY(idmodelo, "ID", "VALIDACAO")

    # Dados do Conjunto de Calibracao
    plsCal = PLSRegression(copy=True, max_iter=500, n_components=nrcomponentes, scale=False, tol=1e-06)
    plsCal.fit(Xcal, Ycal)
    coeficiente = plsCal.score(Xcal, Ycal, sample_weight=None)
    print('score do modelo PLS - Calibracao')
    print(coeficiente)
    print('R2 do modelo PLS - Calibracao')
    coeficienteCal = r2_score(plsCal.predict(Xcal), Ycal)
    print(coeficienteCal)

    # Dados do Conjunto de Validacao
    plsVal = PLSRegression(copy=True, max_iter=500, n_components=nrcomponentes, scale=False, tol=1e-06)
    plsVal.fit(Xval, Yval)
    coeficiente = plsVal.score(Xval, Yval, sample_weight=None)
    print('score do modelo PLS - Validacao')
    print(coeficiente)
    print('R2 do modelo PLS - Validacao')
    coeficienteVal = r2_score(plsVal.predict(Xval), Yval)
    print(coeficienteVal)
    # print('label_ranking_average_precision_score ')
    # print(label_ranking_average_precision_score(np.array(Yval), np.array(plsVal.y_scores_)))

    # Ajustar Calculos do RMSEC
    matYPredCalibracao = []

    for itemMatrizY in YCodigoCal:
      amostra = str(itemMatrizY)
      amostra = amostra.replace("[", "")
      amostra = amostra.replace("]", "")
      # print(i)
      linhaMatriz = []
      amostraPredicao = self.selectAmostra(int(float(amostra)), idmodelo)

      if executaPCA == 'S':
        amostraPredicao = pca.testePCA(amostraPredicao, qtdePC)

      Y_pred = plsCal.predict(amostraPredicao)
      # print(Y_pred)
      linhaMatriz.append(round(np.double(Y_pred), 0))
      matYPredCalibracao += [linhaMatriz]

    rmsec = sqrt(mean_squared_error(Ycal, matYPredCalibracao))
    print('RMSEC')
    print(rmsec)

    # Ajustar Calculos do RMSEP
    matYPredValidacao = []

    for itemMatrizY in YCodigoVal:
      amostra = str(itemMatrizY)
      amostra = amostra.replace("[", "")
      amostra = amostra.replace("]", "")
      # print(i)
      linhaMatriz = []
      amostraPredicao = self.selectAmostra(int(float(amostra)), idmodelo)

      if executaPCA == 'S':
        amostraPredicao = pca.testePCA(amostraPredicao, qtdePC)

      Y_pred = plsVal.predict(amostraPredicao)
      # print(Y_pred)
      linhaMatriz.append(round(np.double(Y_pred), 0))
      matYPredValidacao += [linhaMatriz]

    rmsep = sqrt(mean_squared_error(Yval, matYPredValidacao))
    print('RMSEP')
    print(rmsep)

    # Atualiza valores da calibracao
    db.execute("update calibracao set rmsec = " + str(rmsec) +
               " , inativo = 'A'" +
               " , rmsep = " + str(rmsep) +
               " , coeficientecal = " + str(coeficienteCal) +
               " , coeficienteval = " + str(coeficienteVal) +
               " , dtcalibracao = '" + str(data_em_texto) + "'"
                                                            " where idmodelo = " + str(idmodelo) +
               " and idcalibracao = " + str(idcalibracao) + " ")
    session.commit()

    print("VARIAVEIS LATENTES")
    print(nrcomponentes)

    return idmodelo


def kennardStone(X, k, precomputed=False):
  n = len(X)  # number of samples
  print("Input Size:", n, "Desired Size:", k)
  assert n >= 2 and n >= k and k >= 2, "Error: number of rows must >= 2, k must >= 2 and k must > number of rows"

  # pair-wise distance matrix
  dist = metrics.pairwise_distances(X, metric='euclidean', n_jobs=-1)

  # get the first two samples
  i0, i1 = np.unravel_index(np.argmax(dist, axis=None), dist.shape)
  selected = set([i0, i1])
  k -= 2
  # iterate find the rest
  minj = i0
  while k > 0 and len(selected) < n:
    mindist = 0.0
    for j in range(n):
      if j not in selected:
        mindistj = min([dist[j][i] for i in selected])
        if mindistj > mindist:
          minj = j
          mindist = mindistj
    print(selected, minj, [dist[minj][i] for i in selected])
    selected.add(np.int(minj))
    k -= 1
  print("selected samples indices: ", selected)
  # return selected samples

  return selected
  # if precomputed:
  #    return list(selected)
  # else:
  #    return X[list(selected), :]


pls = PLS()
#pls.predicao(4,101)
# # PARAMETROS
# # IDMODELO, NR_COMPONENTES (VARIAVEIS LATENTES), VALOR DE CORTE OUTLIER, QTDE DE REMOCOES, FAZ PCA S ou N, qtde PC
pls.calibracao(4, 20, 0.4, 4, 'N', 3)


#Valor Utilizado Para a Qualificacao
#pls.calibracao(3, 12, 0.9, 3)

class NumpyEncoder(json.JSONEncoder):
  """ Special json encoder for numpy types """

  def default(self, obj):
    if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                        np.int16, np.int32, np.int64, np.uint8,
                        np.uint16, np.uint32, np.uint64)):
      return int(obj)
    elif isinstance(obj, (np.float_, np.float16, np.float32,
                          np.float64)):
      return float(obj)
    elif isinstance(obj, (np.ndarray,)):  #### This is the fix
      return obj.tolist()
    return json.JSONEncoder.default(self, obj)


'''


print('Erro absoluto mediano')
print(median_absolute_error(Y,matYPred))

print('Erro quadrático log Médio')
print(mean_squared_log_error(Y,matYPred))

print('coverage_error ')
print(coverage_error(np.array(Y),np.array(pls.y_scores_)))

print('label_ranking_average_precision_score ')
print(label_ranking_average_precision_score(np.array(Y),np.array(pls.y_scores_)))

print('label_ranking_loss')
print(label_ranking_loss(np.array(Y),np.array(pls.y_scores_)))

print('explained_variance_score')
print(explained_variance_score(Y,matYPred))


'''


