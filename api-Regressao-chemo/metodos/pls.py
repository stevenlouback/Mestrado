import sys
import numpy as np
import matplotlib.pyplot as plt
import json
from flask import jsonify
from datetime import datetime

sys.path.append("..\dao")

from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import r2_score, mean_squared_error, median_absolute_error, mean_absolute_error, mean_squared_log_error, coverage_error, label_ranking_loss, explained_variance_score, label_ranking_average_precision_score


from sqlalchemy import create_engine

db_string = "postgresql://postgres:postgres@localhost:5432/Quimiometria"

db = create_engine(db_string)


class PLS(object):


    def predicao(self, idmodelo, idamostra):

        idmodelo = idmodelo

        idamostra = idamostra

        print(idmodelo)
        print(idamostra)

        conjunto = "NIR"

        X = self.selectMatrizX(idmodelo, conjunto)
        Y = self.selectMatrizY(idmodelo, conjunto)

        amostraPredicao = self.selectAmostra(idamostra)

        valorReferencia = self.selectDadosReferenciaAmostra(idamostra)

        pls = PLSRegression(copy=True, max_iter=500, n_components=12, scale=False, tol=1e-06)

        pls.fit(X, Y)

        # L = pls.x_loadings_
        # S = pls.x_scores_

        # pls.fit(S, Y)

        Y_pred = pls.predict(amostraPredicao)

        print('Amostra: ' + str(idamostra) + ' - Valor Predito :' + str(Y_pred))

        print('R2 do modelo PLS')
        coeficiente = pls.score(X, Y, sample_weight=None)
        print(coeficiente)
        print(r2_score(pls.predict(X), Y))

        matYPred = []

        for i in range(1, 349):
            #print(i)
            linhaMatriz = []
            idAmostraTestes = i
            amostraPredicao = self.selectAmostra(idamostra)
            Y_pred = pls.predict(amostraPredicao)
            #print(Y_pred)
            linhaMatriz.append(np.double(Y_pred))
            matYPred += [linhaMatriz]

        print('RMSEC')
        # print(mean_squared_error(Y,matYPred))
        raizQ = mean_squared_error(Y, matYPred) ** (1 / 2)
        #print(raizQ)

        ##Grava Predicao
        db.execute(" update matrizy set vlresultado = " + str(1) + " , dtpredicao = '" + str(datetime.now()) + "' where idamostra = 1 and idmodelo = " + str(idmodelo) + "  ")
        db.execute("commit")


        ##Contrucao do JSON
        json_data = jsonify(idamostra=str(idamostra), valorpredito=str(Y_pred), rmsec=str(raizQ), idmodelo=str(idmodelo), valorReferencia=str(valorReferencia), coeficiente=str(coeficiente))

        return json_data

    def selectAmostra(self, idAmostra):

        try:
            #numero de colunas da matriz
            cursorColunas = db.execute("select max(x.nrposicaocoluna) from matrizx x where x.idamostra = " + str(idAmostra) + "  ")

            contadorColunas = 0

            for linha in cursorColunas:
                contadorColunas = linha[0]

            #Preenchimento da MatrizX
            matrizX = []

            cursorAmostras = db.execute("select x.idamostra from matrizx x where x.idamostra =  " + str(idAmostra) + " group by x.idamostra order by x.idamostra asc")

            listaAmostras = []
            for regAmostras in cursorAmostras:
                listaAmostras.append(regAmostras[0])

            #print(listaAmostras)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []



                cursorDadosAmostra = db.execute("SELECT x.idamostra, x.vllinhacoluna FROM matrizx x where x.idamostra = " + str(amostra) + " order by x.idamostra, x.nrsequencia, x.nrposicaolinha, x.nrposicaocoluna asc")

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
            cursorColunas = db.execute(" select max(x.nrposicaocoluna) from matrizx x"
                                       " inner join matrizy y on (x.idamostra = y.idamostra) "
                                       "inner join amostra a on ( a.idamostra = x.idamostra ) "
                                       "where a.tpamostra = '" + str(conjunto) + "' "
                                       " and x.idModelo = " + str(idModelo) + "  ")


            contadorColunas = 0

            for linha in cursorColunas:
                contadorColunas = linha[0]
                print(contadorColunas)

            #Preenchimento da MatrizX
            matrizX = []

            cursorAmostras = db.execute("select x.idamostra from matrizx x  "
                                        "inner join matrizy y on (y.idamostra = x.idamostra) "
                                        "inner join amostra a on ( a.idamostra = x.idamostra ) "
                                        "where a.tpamostra = '" + str(conjunto) + "' "
                                        "group by x.idamostra order by x.idamostra asc")

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
                                                "where x.idamostra = " + str(amostra) + ""
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

    def selectMatrizY(self, idModelo, conjunto):

        try:

            matrizY = []

            cursorAmostras = db.execute("select y.idamostra from matrizy y "
                                        "inner join amostra a on (a.idamostra = y.idamostra) where a.tpamostra = '" + str(conjunto) + "' "
                                        "order by y.idamostra asc")

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

                cursorDadosAmostra = db.execute("select y.idamostra, y.vlreferencia from matrizy y  where "
                                                "y.idamostra = " + str(amostra) + " order by y.idamostra asc")

                for regDadosAmostra in cursorDadosAmostra:
                    if  regDadosAmostra[1] == 0E-8 :
                        linhaMatriz.append('0')
                    else:
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

    def selectDadosReferenciaAmostra(self, idAmostra):

        try:
             cursorDadosAmostra = db.execute("SELECT y.vlreferencia FROM matrizy y where y.idamostra = " + str(idAmostra) + "  ")

             for regDadosAmostra in cursorDadosAmostra:
                valorReferencia = regDadosAmostra[0]

             return valorReferencia
        except Exception:
             return "Ocorreu um erro na busca dos dados"

#pls = PLS()
#pls.predicao(1,348)


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


