import sys
import numpy as np

sys.path.append("..\dao")

from banco import Banco

class Matrizy(object):

    def __init__(self, idAmostra=0, idModelo=0, vlReferencia=0, vlResultado=0, idParametroRef=0, idCalibracao=0, dtPredicao=0):
        self.info = {}
        self.idAmostra = idAmostra
        self.vlReferencia = vlReferencia
        self.vlResultado = vlResultado
        self.idParametroRef = idParametroRef
        self.idCalibracao = idCalibracao
        self.dtPredicao = dtPredicao
        self.idModelo = idModelo

    def select(self, idAmostra):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select idAmostra, idModelo, vlReferencia, vlResultado, idParametroRef, idCalibracao, dtPredicao   from matrizy where idAmostra = " + idAmostra + "  ")

            for linha in c:
                self.idAmostra = linha[0]
                self.idModelo = linha[1]
                self.vlReferencia = linha[2]
                self.vlResultado = linha[3]
                self.idParametroRef = linha[4]
                self.idCalibracao = linha[5]
                self.dtPredicao = linha[6]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca dos dados"

    def selectMatriyYModeloMMM(self, idModelo):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            matrizY = []

            c.execute("select y.idAmostra from matrizy y inner join amostra a on (a.idAmostra = y.idAmostra) order by y.idAmostra asc")

            listaAmostras = []
            for regAmostras in c:
                listaAmostras.append(regAmostras[0])


            print(listaAmostras)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []

                c.execute("select y.idAmostra, y.nrSequencia, y.vlReferencia, y.vlResultado, y.idParametroRef from matrizy y inner join amostra a on (a.idAmostra = y.idAmostra) where a.idAmostra = " + str(amostra) + "  order by y.idAmostra asc")

                for regDadosAmostra in c:
                    linhaMatriz.append(regDadosAmostra[2])
                #print(linhaMatriz)
                    matrizY += [linhaMatriz]


            #print(matrizY)

            c.close()

            return matrizY
        except Exception:
            print(Exception)
            return "Ocorreu um erro na busca dos dados"


    def selectMatrizyYNOVO(self, idModelo, conjunto):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            matrizY = []

            c.execute("select y.idamostra from matrizy y "
                      "inner join amostra a on (a.idamostra = y.idamostra) where a.tpamostra = '" + str(conjunto) + "' "
                      "order by y.idamostra asc")

            listaAmostras = []
            cont = 0
            for regAmostras in c:
                listaAmostras.append(regAmostras[0])
                cont = cont + 1


            #print(listaAmostras)
            print('Qtde de Amostras - Matriz Y')
            print(cont)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []

                c.execute("select y.idamostra, y.vlreferencia from matrizy y  where "
                          "y.idamostra = " + str(amostra) + " order by y.idamostra asc")

                for regDadosAmostra in c:
                    if  regDadosAmostra[1] == 0E-8 :
                        linhaMatriz.append('0')
                    else:
                        linhaMatriz.append(np.double(regDadosAmostra[1]))

                #print(amostra)
                #print(linhaMatriz)
                matrizY += [linhaMatriz]

            #print('MATRIZ - Y')
            #print(matrizY)

            c.close()

            return matrizY
        except Exception:
            print(Exception)
            return "Ocorreu um erro na busca dos dados"