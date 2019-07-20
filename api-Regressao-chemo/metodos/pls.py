import sys
import numpy as np
import matplotlib.pyplot as plt
import json
from math import sqrt
from flask import jsonify
from datetime import datetime
import pandas as pd

sys.path.append("..\dao")

from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import r2_score, mean_squared_error,median_absolute_error, mean_absolute_error, mean_squared_log_error, coverage_error, label_ranking_loss, explained_variance_score, label_ranking_average_precision_score
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from sklearn import metrics

from sqlalchemy import create_engine

db_string = "postgresql://postgres:postgres@localhost:5432/Quimiometria"
#db_string = "postgresql://postgres:postgres@localhost:5432/bkpSteven"

db = create_engine(db_string)

Session = sessionmaker(bind=db)
session = Session()


class PLS(object):


    def predicao(self, idmodelo, idamostra):

        idmodelo = idmodelo

        idamostra = idamostra

        print(idmodelo)
        print(idamostra)

        X = self.selectMatrizX(idmodelo, "CALIBRACAO")
        Y = self.selectMatrizY(idmodelo, "VALOR", "CALIBRACAO")

        amostraPredicao = self.selectAmostra(idamostra, idmodelo)

        valorReferencia = self.selectDadosReferenciaAmostra(idamostra, idmodelo)

        pls = PLSRegression(copy=True, max_iter=500, n_components=20, scale=False, tol=1e-06)

        pls.fit(X, Y)

        valorPredito = pls.predict(amostraPredicao)

        print('Amostra: ' + str(idamostra) + ' - Valor Predito :' + str(valorPredito)+ ' - Valor Referencia :' + str(valorReferencia))

        cursorDadosCalibracao = db.execute("select rmsec, rmsep, coeficiente, dtcalibracao "
                                           "from calibracao where inativo = 'A' and idmodelo = " + str(idmodelo) + " ")
        for regCodigo in cursorDadosCalibracao:
            rmsec = regCodigo[0]
            rmsep = regCodigo[1]
            coeficiente = regCodigo[2]
            dtcalibracao = regCodigo[3]

        print(rmsec)
        print(rmsep)
        print(coeficiente)
        print(dtcalibracao)

        dtcalibracao = dtcalibracao.strftime('%d/%m/%Y')
        print(dtcalibracao)

        #tratamento dos dados para o Json
        coeficiente = round(coeficiente, 2)
        rmsec = round(rmsec, 2)
        rmsep = round(rmsep, 2)
        valorReferencia = round(valorReferencia, 2)

        valorPreditoString = str(valorPredito)
        valorPreditoString = valorPreditoString.replace("[","")
        valorPreditoString = valorPreditoString.replace("]", "")


        ##Contrucao do JSON
        json_data = jsonify(idamostra=str(idamostra), valorpredito=str(valorPreditoString),
                            rmsec=str(rmsec), rmsep=str(rmsep), idmodelo=str(idmodelo),  dtcalibracao=str(dtcalibracao),
                            valorreferencia=str(valorReferencia), coeficiente=str(coeficiente))

        return json_data

    def selectAmostra(self, idAmostra, idmodelo):

        try:
            #numero de colunas da matriz
            cursorColunas = db.execute("select max(x.nrposicaocoluna) from matrizx x where x.idamostra = " + str(idAmostra) + "  and x.idmodelo = " + str(idmodelo) + "")

            contadorColunas = 0

            for linha in cursorColunas:
                contadorColunas = linha[0]

            #Preenchimento da MatrizX
            matrizX = []

            cursorAmostras = db.execute("select x.idamostra from matrizx x "
                                        "where x.idamostra =  " + str(idAmostra) + ""
                                        "  and x.idmodelo = " + str(idmodelo) + ""
                                        " group by x.idamostra order by x.idamostra asc")

            listaAmostras = []
            for regAmostras in cursorAmostras:
                listaAmostras.append(regAmostras[0])

            #print(listaAmostras)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []



                cursorDadosAmostra = db.execute("SELECT x.idamostra, x.vllinhacoluna FROM matrizx x "
                                                "where x.idamostra = " + str(amostra) + "" 
                                                 "  and x.idmodelo = " + str(idmodelo) + ""
                                                " order by x.idamostra, x.nrsequencia, x.nrposicaolinha, x.nrposicaocoluna asc")

                for regDadosAmostra in cursorDadosAmostra:
                    if  regDadosAmostra[1] == 0E-8 :
                        linhaMatriz.append('0')
                    else:
                        linhaMatriz.append(regDadosAmostra[1])
                        #x=Symbol('x')
                        #difx = diff(regDadosAmostra[1], x)
                        #linhaMatriz.append(difx)

                #print(amostra)
                #print(linhaMatriz)
                matrizX += [linhaMatriz]

            #print('AMOSTRA SELECIONADA')
            #print(matrizX)


            return matrizX
        except Exception:
            #print(Exception)
            return "Ocorreu um erro na busca dos dados"

    def selectMatrizX(self, idModelo, conjunto):

        try:
            #numero de colunas da matriz

            if conjunto == "TODOS":
                sqlConsulta = (" inner join matrizy y on (x.idamostra = y.idamostra and y.idmodelo = x.idmodelo) "
                              "inner join amostra a on ( a.idamostra = x.idamostra and a.idmodelo = x.idmodelo ) ")
                whereConsulta = ("where x.idModelo = " + str(idModelo) + "  ")

            elif conjunto == "CALIBRACAO":
                sqlConsulta = (" inner join matrizy y on (x.idamostra = y.idamostra and y.idmodelo = x.idmodelo) "
                              "inner join amostra a on ( a.idamostra = x.idamostra and a.idmodelo = x.idmodelo ) "
                              "inner join amostra_calibracao ac on ( a.idamostra = ac.idamostra and a.idmodelo = ac.idmodelo ) "
                              "inner join calibracao c on ( c.idcalibracao = ac.idcalibracao and c.inativo = 'A' ) ")
                whereConsulta = ("where x.idModelo = " + str(idModelo) + " and ac.tpconjunto = 'CALIBRACAO' ")

            elif conjunto == "VALIDACAO":
                sqlConsulta = (" inner join matrizy y on (x.idamostra = y.idamostra and y.idmodelo = x.idmodelo) "
                              "inner join amostra a on ( a.idamostra = x.idamostra and a.idmodelo = x.idmodelo ) "
                              "inner join amostra_calibracao ac on ( a.idamostra = ac.idamostra and a.idmodelo = ac.idmodelo ) "
                              "inner join calibracao c on ( c.idcalibracao = ac.idcalibracao and c.inativo = 'A' ) ")
                whereConsulta = ("where x.idModelo = " + str(idModelo) + " and ac.tpconjunto = 'VALIDACAO' ")


            sqlColunas = (" select max(x.nrposicaocoluna) from matrizx x " + str(sqlConsulta) + " " + str(whereConsulta) + " ")
            cursorColunas = db.execute(sqlColunas)

            contadorColunas = 0

            for linha in cursorColunas:
                contadorColunas = linha[0]
                print(contadorColunas)

            #Preenchimento da MatrizX
            matrizX = []

            sqlListaAmostras = ("select x.idamostra from matrizx x  " + str(sqlConsulta) + str(whereConsulta) + "group by x.idamostra order by x.idamostra asc")
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

            print('Qtde de Amostras - Matriz X')
            print(cont)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []

                cursorDadosAmostra = db.execute("SELECT idamostra, vllinhacoluna 	FROM matrizx x "
                                                "where x.idamostra = " + str(amostra) + " and x.idModelo = " + str(idModelo) + ""
                                                "order by x.idamostra, x.nrsequencia, x.nrposicaolinha, x.nrposicaocoluna asc")

                for regDadosAmostra in cursorDadosAmostra:
                    if  regDadosAmostra[1] == 0E-8 :
                        linhaMatriz.append('0')
                    else:
                        linhaMatriz.append(regDadosAmostra[1])
                        #x=Symbol('x')
                        #difx = diff(regDadosAmostra[1], x)
                        #linhaMatriz.append(difx)




                #print(amostra)
                #print(linhaMatriz)
                matrizX += [linhaMatriz]

            #print('MATRIZ - X')
            #print(matrizX)

            return matrizX
        except Exception:
            print(Exception)
            return "Ocorreu um erro na busca dos dados"

    def selectMatrizY(self, idmodelo, tipo, conjunto):

        try:
            if conjunto == "TODOS":
                sqlConsulta = ("inner join amostra a on (a.idamostra = y.idamostra and a.idmodelo = y.idmodelo) ")
                whereConsulta = (" where y.idmodelo = " + str(idmodelo) + " " )

            elif conjunto == "CALIBRACAO":
                sqlConsulta = (" inner join amostra a on (a.idamostra = y.idamostra and a.idmodelo = y.idmodelo) " 
                              "inner join amostra_calibracao ac on ( a.idamostra = ac.idamostra and a.idmodelo = ac.idmodelo ) "
                              "inner join calibracao c on ( c.idcalibracao = ac.idcalibracao and c.inativo = 'A' ) ")
                whereConsulta = (" where y.idModelo = " + str(idmodelo) + " and ac.tpconjunto = 'CALIBRACAO' ")

            elif conjunto == "VALIDACAO":
                sqlConsulta = (" inner join amostra a on (a.idamostra = y.idamostra and a.idmodelo = y.idmodelo) " 
                              "inner join amostra_calibracao ac on ( a.idamostra = ac.idamostra and a.idmodelo = ac.idmodelo ) "
                              "inner join calibracao c on ( c.idcalibracao = ac.idcalibracao and c.inativo = 'A' ) ")
                whereConsulta = (" where y.idModelo = " + str(idmodelo) + " and ac.tpconjunto = 'VALIDACAO' ")



            matrizY = []

            sqlListaAmostras= ("select y.idamostra from matrizy y " + str(sqlConsulta) + " " + str(whereConsulta) + " order by y.idamostra asc" )
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


            #print(listaAmostras)
            print('Qtde de Amostras - Matriz Y')
            print(cont)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []

                cursorDadosAmostra = db.execute("select y.idamostra, y.vlreferencia from matrizy y "
                                                " where y.idamostra = " + str(amostra)  + " "
                                                " and y.idmodelo = " + str(idmodelo) + " "
                                                " order by y.idamostra asc")

                for regDadosAmostra in cursorDadosAmostra:
                    if  regDadosAmostra[1] == 0E-8 :
                        linhaMatriz.append('0')
                    else:
                        if tipo == "ID" :
                            linhaMatriz.append(regDadosAmostra[0])
                        if tipo == "VALOR":
                            linhaMatriz.append(np.double(regDadosAmostra[1]))

                #print(amostra)
                #print(linhaMatriz)
                matrizY += [linhaMatriz]

            #print('MATRIZ - Y')
            #print(matrizY)

            return matrizY
        except Exception:
            print(Exception)
            return "Ocorreu um erro na busca dos dados"

    def selectDadosReferenciaAmostra(self, idAmostra, idmodelo):

        try:
             cursorDadosAmostra = db.execute("SELECT y.vlreferencia FROM matrizy y where y.idamostra = " + str(idAmostra) + "  and y.idmodelo =  "+ str(idmodelo) + "")

             for regDadosAmostra in cursorDadosAmostra:
                valorReferencia = regDadosAmostra[0]

             return valorReferencia
        except Exception:
             return "Ocorreu um erro na busca dos dados"


    def calibracao(self, idmodelo, nrcomponentes):

        #Inativa calibracoes anteriores
        db.execute("update calibracao set  inativo = 'F'" +
                   " where idmodelo = " + str(idmodelo) + " ")
        session.commit()

        #cria calibracao para o modelo
        data_Atual = datetime.today()
        data_em_texto = data_Atual.strftime('%d/%m/%Y')

        cursorCodigo = db.execute("select coalesce(max(idcalibracao),0) + 1 as codigo from calibracao where idmodelo = " + str(idmodelo) + " ")
        for regCodigo in cursorCodigo:
            idcalibracao = regCodigo[0]


        db.execute("insert into calibracao (idcalibracao, idmodelo, dtcalibracao, inativo) "
                   "values (" +str(idcalibracao) + ","+str(idmodelo)+" , '" + str(data_em_texto) +"', 'A' )")
        session.commit()

        idmodelo = idmodelo

        print(idmodelo)

        Xtodos = self.selectMatrizX(idmodelo, "TODOS")

        #caso seja necessario PCA
        #pca = PCA()
        #pca.testePCA(X)


        #***************************************************************************************************************
        #inicio kennard-stone
        data = pd.DataFrame(Xtodos)
        number_of_samples = Xtodos.__len__()
        number_of_samples = number_of_samples * 0.75
        number_of_selected_samples = 20

        # generate samples 0f samples for demonstration
        #XX = np.random.rand(number_of_samples, 2)

        # standarize X
        #autoscaled_X = (X - X.mean(axis=0)) / X.std(axis=0, ddof=1)

        #selected_sample_numbers, remaining_sample_numbers = kennardstonealgorithm(X, number_of_samples)
        amostras_Calibracao = kennardStone(Xtodos, number_of_samples)
        print("amostras_Calibracao")
        print(amostras_Calibracao)
        print("---")
        print("remaining sample numbers")
        #print(remaining_sample_numbers)

        """#plot samples
        plt.figure()
        plt.scatter(autoscaled_X[:, 0], autoscaled_X[:, 1], label="all samples")
        plt.scatter(autoscaled_X[selected_sample_numbers, 0], autoscaled_X[selected_sample_numbers, 1], marker="*",
                    label="all samples")
        plt.xlabel("x1")
        plt.ylabel("x2")
        plt.legend(loc='upper right')
        plt.show()
        
        
        #***************************************************************************************************************
        #fim kennard-stone"""

        # Insercao das amostras de Validacao
        YCodigoTodos = self.selectMatrizY(idmodelo, "ID", "TODOS")

        for amostraX in YCodigoTodos:
            amostra = str(amostraX)
            amostra = amostra.replace("[", "")
            amostra = amostra.replace("]", "")
            db.execute("insert into amostra_calibracao (idcalibracao, idmodelo, idamostra, tpconjunto) "
                       "values (" + str(idcalibracao) + "," + str(idmodelo) + " , '" + str(int(float(amostra))) + "','VALIDACAO' )")

        session.commit()

        #Insercao das amostras de Calibracao
        for amostraCalibracao in amostras_Calibracao:
            amostra = str(amostraCalibracao)
            amostra = amostra.replace("[", "")
            amostra = amostra.replace("]", "")
            db.execute("update  amostra_calibracao set tpconjunto = 'CALIBRACAO'  "
                       " where idcalibracao =" + str(idcalibracao) + " and idmodelo = " + str(idmodelo) +
                       " and idamostra = " + str(int(float(amostra))))
        session.commit()


        Xcal = self.selectMatrizX(idmodelo, "CALIBRACAO")
        Xval = self.selectMatrizX(idmodelo, "VALIDACAO")

        Ycal = self.selectMatrizY(idmodelo, "VALOR", "CALIBRACAO")
        Yval = self.selectMatrizY(idmodelo, "VALOR", "VALIDACAO")

        YCodigoCal = self.selectMatrizY(idmodelo, "ID", "CALIBRACAO")
        YCodigoVal = self.selectMatrizY(idmodelo, "ID", "VALIDACAO")


        #Dados do Conjunto de Calibracao
        pls = PLSRegression(copy=True, max_iter=500, n_components=nrcomponentes, scale=False, tol=1e-06)
        pls.fit(Xcal, Ycal)
        coeficiente = pls.score(Xcal, Ycal, sample_weight=None)
        print('R2 do modelo PLS - Calibracao')
        print(coeficiente)
        print(r2_score(pls.predict(Xcal),Ycal))

        # Dados do Conjunto de Validacao
        pls = PLSRegression(copy=True, max_iter=500, n_components=nrcomponentes, scale=False, tol=1e-06)
        pls.fit(Xval, Yval)
        coeficiente = pls.score(Xval, Yval, sample_weight=None)
        print('R2 do modelo PLS - Validacao')
        print(coeficiente)
        print(r2_score(pls.predict(Xval), Yval))


        #Ajustar Calculos do RMSEC
        matYPredCalibracao = []

        for itemMatrizY in YCodigoCal:
            amostra = str(itemMatrizY)
            amostra = amostra.replace("[", "")
            amostra = amostra.replace("]", "")
            # print(i)
            linhaMatriz = []
            amostraPredicao = self.selectAmostra(int(float(amostra)), idmodelo)
            Y_pred = pls.predict(amostraPredicao)
            # print(Y_pred)
            linhaMatriz.append(np.double(Y_pred))
            matYPredCalibracao += [linhaMatriz]

        rmsec = sqrt(mean_squared_error(Ycal, matYPredCalibracao))
        print('RMSEC')
        print(rmsec)

        #Ajustar Calculos do RMSEP
        matYPredValidacao = []

        for itemMatrizY in YCodigoVal:
            amostra = str(itemMatrizY)
            amostra = amostra.replace("[", "")
            amostra = amostra.replace("]", "")
            # print(i)
            linhaMatriz = []
            amostraPredicao = self.selectAmostra(int(float(amostra)), idmodelo)
            Y_pred = pls.predict(amostraPredicao)
            # print(Y_pred)
            linhaMatriz.append(np.double(Y_pred))
            matYPredValidacao += [linhaMatriz]

        rmsep = sqrt(mean_squared_error(Yval, matYPredValidacao))
        print('RMSEP')
        print(rmsep)

        #Atualiza valores da calibracao
        db.execute("update calibracao set rmsec = " + str(rmsec) +
                   " , inativo = 'A'" +
                   " , rmsep = " + str(rmsep) +
                   " , coeficiente = " + str(coeficiente) +
                   " , dtcalibracao = '" + str(data_em_texto) + "'"
                   " where idmodelo = " + str(idmodelo) +
                   " and idcalibracao = " + str(idcalibracao) + " ")
        session.commit()


        return idmodelo

def kennardStone(X, k, precomputed=False):
    n = len(X) # number of samples
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
        selected.add(minj)
        k -= 1
    print("selected samples indices: ", selected)
    # return selected samples


    return selected
    #if precomputed:
    #    return list(selected)
    #else:
    #    return X[list(selected), :]


pls = PLS()
#pls.predicao(1,300)
pls.calibracao(2, 20)


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
        elif isinstance(obj,(np.ndarray,)): #### This is the fix
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


