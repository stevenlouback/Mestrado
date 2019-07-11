import sys
import numpy as np
import matplotlib.pyplot as plt
import json
from math import sqrt
from flask import jsonify
from datetime import datetime

sys.path.append("..\dao")

from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import r2_score, mean_squared_error, median_absolute_error, mean_absolute_error, mean_squared_log_error, coverage_error, label_ranking_loss, explained_variance_score, label_ranking_average_precision_score
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

from sqlalchemy import create_engine

db_string = "postgresql://postgres:postgres@localhost:5432/Quimiometria"

db = create_engine(db_string)

Session = sessionmaker(bind=db)
session = Session()


class PLS(object):


    def predicao(self, idmodelo, idamostra):

        idmodelo = idmodelo

        idamostra = idamostra

        print(idmodelo)
        print(idamostra)

        conjunto = "CALIBRACAO"

        X = self.selectMatrizX(idmodelo, conjunto)
        Y = self.selectMatrizY(idmodelo, conjunto, "VALOR")

        amostraPredicao = self.selectAmostra(idamostra, idmodelo)

        valorReferencia = self.selectDadosReferenciaAmostra(idamostra, idmodelo)

        pls = PLSRegression(copy=True, max_iter=500, n_components=12, scale=False, tol=1e-06)

        pls.fit(X, Y)

        valorPredito = pls.predict(amostraPredicao)

        print('Amostra: ' + str(idamostra) + ' - Valor Predito :' + str(valorPredito))


        coeficiente = pls.score(X, Y, sample_weight=None)
        print('R2 do modelo PLS')
        print(coeficiente)
        print(r2_score(pls.predict(X), Y))


        #Ajustar Calculos do RMSEC e RMSEP para ficarem dinamicos
        matYPred = []

        for i in range(1, 349):
            #print(i)
            linhaMatriz = []
            idAmostraTestes = i
            amostraPredicao = self.selectAmostra(idamostra, idmodelo)
            Y_pred = pls.predict(amostraPredicao)
            #print(Y_pred)
            linhaMatriz.append(np.double(Y_pred))
            matYPred += [linhaMatriz]


        # print(mean_squared_error(Y,matYPred))
        raizQ = mean_squared_error(Y, matYPred) ** (1 / 2)

        rms = sqrt(mean_squared_error(Y, matYPred))
        print('RMSEC')
        print(raizQ)
        print(rms)


        #tratamento dos dados para o Json
        coeficiente = round(coeficiente, 2)
        #valorPredito = round(valorPredito, 2)
        raizQ = round(raizQ, 2)
        valorReferencia = round(valorReferencia, 2)

        valorPreditoString = str(valorPredito)
        valorPreditoString = valorPreditoString.replace("[","")
        valorPreditoString = valorPreditoString.replace("]", "")


        ##Contrucao do JSON
        json_data = jsonify(idamostra=str(idamostra), valorpredito=str(valorPreditoString), rmsec=str(raizQ), idmodelo=str(idmodelo), valorreferencia=str(valorReferencia), coeficiente=str(coeficiente))

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
                                        " and x.idModelo = " + str(idModelo) + "  "                                                                                  
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

    def selectMatrizY(self, idmodelo, conjunto, tipo):

        try:

            matrizY = []

            cursorAmostras = db.execute("select y.idamostra from matrizy y "
                                        "inner join amostra a on (a.idamostra = y.idamostra) where a.tpamostra = '" + str(conjunto) + "' "
                                        " and y.idmodelo = " + str(idmodelo) + " "                                                                                              
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

                cursorDadosAmostra = db.execute("select y.idamostra, y.vlreferencia from matrizy y "
                                                " where y.idamostra = " + str(amostra)  + " "
                                                " and y.idmodelo = " + str(idmodelo) + " "
                                                " order by y.idamostra asc")

                for regDadosAmostra in cursorDadosAmostra:
                    if  regDadosAmostra[1] == 0E-8 :
                        linhaMatriz.append('0')
                    else:
                        if tipo == "ID" :
                            linhaMatriz.append(np.double(regDadosAmostra[0]))
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


    def calibracao(self, idmodelo):

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


        db.execute("insert into calibracao (idcalibracao, idmodelo, dtcalibracao) "
                   "values (" +str(idcalibracao) + ","+str(idmodelo)+" , '" + str(data_em_texto) +"' )")
        session.commit()

        idmodelo = idmodelo

        print(idmodelo)

        conjunto = "CALIBRACAO"

        X = self.selectMatrizX(idmodelo, conjunto)
        Y = self.selectMatrizY(idmodelo, conjunto, "VALOR")
        YCodigo = self.selectMatrizY(idmodelo, conjunto, "ID")

        pls = PLSRegression(copy=True, max_iter=500, n_components=12, scale=False, tol=1e-06)
        pls.fit(X, Y)

        coeficiente = pls.score(X, Y, sample_weight=None)
        print('R2 do modelo PLS')
        print(coeficiente)
        print(r2_score(pls.predict(X), Y))

        #Ajustar Calculos do RMSEC e RMSEP para ficarem dinamicos
        matYPred = []

        for item in YCodigo:
            #print(i)
            linhaMatriz = []
            amostra = str(item)
            amostra = amostra.replace("[", "")
            amostra = amostra.replace("]", "")
            amostraPredicao = self.selectAmostra(int(float(amostra)), idmodelo)
            Y_pred = pls.predict(amostraPredicao)
            #print(Y_pred)
            linhaMatriz.append(np.double(Y_pred))
            matYPred += [linhaMatriz]
            db.execute("insert into amostra_calibracao (idcalibracao, idmodelo, idamostra) "
                       "values (" + str(idcalibracao) + "," + str(idmodelo) + " , '" + str(int(float(amostra))) + "' )")

        session.commit()

        # print(mean_squared_error(Y,matYPred))
        raizQ = mean_squared_error(Y, matYPred) ** (1 / 2)

        rms = sqrt(mean_squared_error(Y, matYPred))
        print('RMSEC')
        print(raizQ)
        print(rms)

        #Atualiza valores da calibracao
        db.execute("update calibracao set rmsec = " + str(rms) +
                   " , inativo = 'A'" +
                   " , rmsep = " + str(rms) +
                   " , coeficiente = " + str(coeficiente) +
                   " , dtcalibracao = '" + str(data_em_texto) + "'"
                   " where idmodelo = " + str(idmodelo) +
                   " and idcalibracao = " + str(idcalibracao) + " ")
        session.commit()


        return idmodelo


pls = PLS()
#pls.predicao(1,348)
pls.calibracao(1)


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


