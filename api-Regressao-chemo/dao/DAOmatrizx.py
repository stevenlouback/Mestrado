import sys
import numpy as np
from sympy import *

sys.path.append("..\dao")

from banco import Banco


class Matrizx(object):

    def __init__(self, idAmostra=0, nrSequencia=0, nrPosicaoLinha=0, nrPosicaoColuna=0, vlLinhaColuna=0, idModelo=0):
        self.info = {}
        self.idAmostra = idAmostra
        self.nrSequencia = nrSequencia
        self.nrPosicaoLinha = nrPosicaoLinha
        self.nrPosicaoColuna = nrPosicaoColuna
        self.vlLinhaColuna = vlLinhaColuna
        self.idModelo = idModelo

    def select(self, idAmostra):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select idAmostra, nrSequencia, nrPosicaoLinha, nrPosicaoColuna, vlLinhaColuna, idModelo from matrizx where idAmostra = " + idAmostra + "  ")

            for linha in c:
                self.idAmostra = linha[0]
                self.nrSequencia = linha[1]
                self.nrPosicaoLinha = linha[2]
                self.nrPosicaoColuna = linha[3]
                self.vlLinhaColuna = linha[4]
                self.idModelo = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca dos dados"

    def selectMatrizXModelo(self, idModelo):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c2 = banco.conexao.cursor()

            #numero de colunas da matriz
            c.execute("select max(x.nrPosicaoColuna) from matrizx x inner join amostra a on (a.idAmostra = x.idAmostra) where a.idModelo = " + idModelo + "  ")

            contadorColunas = 0

            for linha in c:
                contadorColunas = linha[0]

            #Preenchimento da MatrizX
            matrizX = []


            c.execute("select x.idAmostra from matrizx x inner join amostra a on (a.idAmostra = x.idAmostra) where a.idModelo =  " + str(idModelo) + " group by x.idAmostra order by x.idAmostra asc")

            listaAmostras = []
            for regAmostras in c:
                listaAmostras.append(regAmostras[0])


            print(listaAmostras)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []

                c.execute("select x.idAmostra, x.nrSequencia, x.nrPosicaoLinha, x.nrPosicaoColuna, x.vlLinhaColuna from matrizx x inner join amostra a on (a.idAmostra = x.idAmostra) where a.idAmostra = " + str(amostra) + "  order by x.nrPosicaoLinha asc, x.nrPosicaoColuna asc")

                for regDadosAmostra in c:
                    linhaMatriz.append(regDadosAmostra[4])
                #print(linhaMatriz)
                matrizX += [linhaMatriz]


            print(matrizX)

            c.close()

            return "Busca feita com sucesso!"
        except Exception:
            print(Exception)
            return "Ocorreu um erro na busca dos dados"

    def selectMatrizXModeloMMM(self, idModelo):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c2 = banco.conexao.cursor()

            #numero de colunas da matriz
            c.execute("select max(x.nrPosicaoColuna) from matrizx x inner join amostra a on (a.idAmostra = x.idAmostra) where a.idModelo = " + idModelo + "  ")

            contadorColunas = 0

            for linha in c:
                contadorColunas = linha[0]

            #Preenchimento da MatrizX
            matrizX = []


            c.execute("select x.idAmostra from matrizx x inner join amostra a on (a.idAmostra = x.idAmostra) where a.idModelo =  " + str(idModelo) + " group by x.idAmostra order by x.idAmostra asc")

            listaAmostras = []
            for regAmostras in c:
                listaAmostras.append(regAmostras[0])


            print(listaAmostras)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []

                c.execute("select x.idAmostra, x.nrSequencia, x.nrPosicaoLinha, x.nrPosicaoColuna, x.vlLinhaColuna from matrizx x inner join amostra a on (a.idAmostra = x.idAmostra) where a.idAmostra = " + str(amostra) + "  order by x.nrPosicaoLinha asc, x.nrPosicaoColuna asc")

                for regDadosAmostra in c:
                    linhaMatriz.append(regDadosAmostra[4])
                #print(linhaMatriz)
                matrizX += [linhaMatriz]


            #print(matrizX)

            c.close()

            return matrizX
        except Exception:
            print(Exception)
            return "Ocorreu um erro na busca dos dados"

    def selectMatrizXModeloNOVO(self, idModelo, conjunto):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c2 = banco.conexao.cursor()

            #numero de colunas da matriz
#            c.execute("select max(x.nrcoluna) from matrizamostra x where x.idModelo = " + str(idModelo) + "  ")
            c.execute(" select max(x.nrposicaocoluna) from matrizx x"
                      " inner join matrizy y on (x.idamostra = y.idamostra) "
                      "inner join amostra a on ( a.idamostra = x.idamostra ) "
                      "where a.tpamostra = '" + str(conjunto) + "' "
                      " and x.idModelo = " + str(idModelo) + "  ")

            contadorColunas = 0

            for linha in c:
                contadorColunas = linha[0]
                print(contadorColunas)

            #Preenchimento da MatrizX
            matrizX = []

            c.execute("select x.idamostra from matrizx x  "
                      "inner join matrizy y on (y.idamostra = x.idamostra) "
                      "inner join amostra a on ( a.idamostra = x.idamostra ) "
                      "where a.tpamostra = '" + str(conjunto) + "' "
                      "group by x.idamostra order by x.idamostra asc")

            cont = 0
            listaAmostras = []
            for regAmostras in c:
                listaAmostras.append(regAmostras[0])
                cont = cont + 1

            print('Qtde de Amostras - Matriz X')
            print(cont)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []

                c.execute("SELECT idamostra, vllinhacoluna 	FROM matrizx x "
                          "where x.idamostra = " + str(amostra) + ""
                            "order by x.idamostra, x.nrsequencia, x.nrposicaolinha, x.nrposicaocoluna asc")

                for regDadosAmostra in c:
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

            print('MATRIZ - X')
            print(matrizX)

            c.close()

            return matrizX
        except Exception:
            print(Exception)
            return "Ocorreu um erro na busca dos dados"

    def selectAmostra(self, idAmostra):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c2 = banco.conexao.cursor()

            #numero de colunas da matriz
            c.execute("select max(x.nrposicaocoluna) from matrizx x where x.idamostra = " + str(idAmostra) + "  ")

            contadorColunas = 0

            for linha in c:
                contadorColunas = linha[0]

            #Preenchimento da MatrizX
            matrizX = []


            c.execute("select x.idamostra from matrizx x where x.idamostra =  " + str(idAmostra) + " group by x.idamostra order by x.idamostra asc")

            listaAmostras = []
            for regAmostras in c:
                listaAmostras.append(regAmostras[0])

            #print(listaAmostras)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []



                c.execute("SELECT x.idamostra, x.vllinhacoluna FROM matrizx x where x.idamostra = " + str(amostra) + " order by x.idamostra, x.nrsequencia, x.nrposicaolinha, x.nrposicaocoluna asc")

                for regDadosAmostra in c:
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

            c.close()

            return matrizX
        except Exception:
            print(Exception)
            return "Ocorreu um erro na busca dos dados"
