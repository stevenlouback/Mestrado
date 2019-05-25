import sys
import numpy as np

sys.path.append("..\conexaoBanco")

from banco import Banco

class Matrizx(object):

    def __init__(self, idAmostra=0, nrSequencia=0, nrPosicaoLinha=0, nrPosicaoColuna=0, vlLinhaColuna=0):
        self.info = {}
        self.idAmostra = idAmostra
        self.nrSequencia = nrSequencia
        self.nrPosicaoLinha = nrPosicaoLinha
        self.nrPosicaoColuna = nrPosicaoColuna
        self.vlLinhaColuna = vlLinhaColuna

    def insert(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into Matriz_x (idAmostra, nrSequencia, nrPosicaoLinha, nrPosicaoColuna, vlLinhaColuna) values ( " +self.idAmostra+ "," + self.nrSequencia + ", " + self.nrPosicaoLinha + ", " + self.nrPosicaoColuna + ", " + self.vlLinhaColuna + " )")

            banco.conexao.commit()
            c.close()

            return "Linha cadastrada com sucesso!"
        except:
            return "Ocorreu um erro na inserção da Amostra"

    def select(self, idAmostra):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select idAmostra, nrSequencia, nrPosicaoLinha, nrPosicaoColuna, vlLinhaColuna from matriz_x where idAmostra = " + idAmostra + "  ")

            for linha in c:
                self.idAmostra = linha[0]
                self.nrSequencia = linha[1]
                self.nrPosicaoLinha = linha[2]
                self.nrPosicaoColuna = linha[3]
                self.vlLinhaColuna = linha[4]

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
            c.execute("select max(x.nrPosicaoColuna) from matriz_x x inner join amostra a on (a.idAmostra = x.idAmostra) where a.idModelo = " + idModelo + "  ")

            contadorColunas = 0

            for linha in c:
                contadorColunas = linha[0]

            #Preenchimento da MatrizX
            matrizX = []


            c.execute("select x.idAmostra from matriz_x x inner join amostra a on (a.idAmostra = x.idAmostra) where a.idModelo =  " + str(idModelo) + " group by x.idAmostra order by x.idAmostra asc")

            listaAmostras = []
            for regAmostras in c:
                listaAmostras.append(regAmostras[0])


            print(listaAmostras)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []

                c.execute("select x.idAmostra, x.nrSequencia, x.nrPosicaoLinha, x.nrPosicaoColuna, x.vlLinhaColuna from matriz_x x inner join amostra a on (a.idAmostra = x.idAmostra) where a.idAmostra = " + str(amostra) + "  order by x.nrPosicaoLinha asc, x.nrPosicaoColuna asc")

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
            c.execute("select max(x.nrPosicaoColuna) from matriz_x x inner join amostra a on (a.idAmostra = x.idAmostra) where a.idModelo = " + idModelo + "  ")

            contadorColunas = 0

            for linha in c:
                contadorColunas = linha[0]

            #Preenchimento da MatrizX
            matrizX = []


            c.execute("select x.idAmostra from matriz_x x inner join amostra a on (a.idAmostra = x.idAmostra) where a.idModelo =  " + str(idModelo) + " group by x.idAmostra order by x.idAmostra asc")

            listaAmostras = []
            for regAmostras in c:
                listaAmostras.append(regAmostras[0])


            print(listaAmostras)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []

                c.execute("select x.idAmostra, x.nrSequencia, x.nrPosicaoLinha, x.nrPosicaoColuna, x.vlLinhaColuna from matriz_x x inner join amostra a on (a.idAmostra = x.idAmostra) where a.idAmostra = " + str(amostra) + "  order by x.nrPosicaoLinha asc, x.nrPosicaoColuna asc")

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

    def selectMatrizXModeloNOVO(self, idModelo):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c2 = banco.conexao.cursor()

            #numero de colunas da matriz
            #c.execute("select max(x.nrcoluna) from matrizamostra x where x.idModelo = " + str(idModelo) + "  ")
            c.execute("select max(x.nrcoluna) from matrizamostra x inner join amostratestes y on (y.idamostratestes = x.idamostratestes) where y.tipoamostra = 'CALIBRA' ")

            contadorColunas = 0

            for linha in c:
                contadorColunas = linha[0]

            #Preenchimento da MatrizX
            matrizX = []


            c.execute("select x.idamostratestes from matrizamostra x  inner join amostratestes y on (y.idamostratestes = x.idamostratestes)  where x.idamostratestes > 100000 and y.tipoamostra = 'CALIBRA'  group by x.idamostratestes order by x.idamostratestes asc ")

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

                c.execute("SELECT idamostratestes, vlresultado 	FROM public.matrizamostra where idamostratestes = " + str(amostra) + " order by idamostratestes, nrsequencia, 	nrlinha, nrcoluna, dsidentifica asc")

                for regDadosAmostra in c:
                    if  regDadosAmostra[1] == 0E-8 :
                        linhaMatriz.append('0')
                    else:
                        linhaMatriz.append(np.double(regDadosAmostra[1]))

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

    def selectAmostra(self, idAmostra):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c2 = banco.conexao.cursor()

            #numero de colunas da matriz
            c.execute("select max(x.nrcoluna) from matrizamostra x where x.idamostratestes = " + str(idAmostra) + "  ")

            contadorColunas = 0

            for linha in c:
                contadorColunas = linha[0]

            #Preenchimento da MatrizX
            matrizX = []


            c.execute("select x.idamostratestes from matrizamostra x where x.idamostratestes =  " + str(idAmostra) + " group by x.idamostratestes order by x.idamostratestes asc")

            listaAmostras = []
            for regAmostras in c:
                listaAmostras.append(regAmostras[0])

            #print(listaAmostras)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []

                c.execute("SELECT idamostratestes, vlresultado 	FROM public.matrizamostra where idamostratestes = " + str(amostra) + " order by idamostratestes, nrsequencia, 	nrlinha, nrcoluna, dsidentifica asc")

                for regDadosAmostra in c:
                    if  regDadosAmostra[1] == 0E-8 :
                        linhaMatriz.append('0')
                    else:
                        linhaMatriz.append(regDadosAmostra[1])

                print(amostra)
                print(linhaMatriz)
                matrizX += [linhaMatriz]

            #print('MATRIZ - X')
            #print(matrizX)

            c.close()

            return matrizX
        except Exception:
            print(Exception)
            return "Ocorreu um erro na busca dos dados"