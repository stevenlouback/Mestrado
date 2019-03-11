import sys

sys.path.append("..\conexaoBanco")

from banco import Banco

class Matrizy(object):

    def __init__(self, idAmostra=0, nrSequencia=0, vlReferencia=0, vlResultado=0, idParametroRef=0):
        self.info = {}
        self.idAmostra = idAmostra
        self.nrSequencia = nrSequencia
        self.vlReferencia = vlReferencia
        self.vlResultado = vlResultado
        self.idParametroRef = idParametroRef

    def insert(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into Matriz_y (idAmostra, nrSequencia, vlReferencia, vlResultado, idParametroRef) values ( " +self.idAmostra+ "," + self.nrSequencia + ", " + self.vlReferencia + ", " + self.vlResultado + ", " + self.idParametroRef + " )")

            banco.conexao.commit()
            c.close()

            return "Parametro cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção da Amostra"

    def select(self, idAmostra):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select idAmostra, nrSequencia, vlReferencia, vlResultado, idParametroRef from matriz_y where idAmostra = " + idAmostra + "  ")

            for linha in c:
                self.idAmostra = linha[0]
                self.nrSequencia = linha[1]
                self.vlReferencia = linha[2]
                self.vlResultado = linha[3]
                self.idParametroRef = linha[4]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca dos dados"

    def selectMatrizYModelo(self, idModelo):
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

    def selectMatriyYModeloMMM(self, idModelo):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            matrizY = []

            c.execute("select y.idAmostra from matriz_y y inner join amostra a on (a.idAmostra = y.idAmostra) order by y.idAmostra asc")

            listaAmostras = []
            for regAmostras in c:
                listaAmostras.append(regAmostras[0])


            print(listaAmostras)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []

                c.execute("select y.idAmostra, y.nrSequencia, y.vlReferencia, y.vlResultado, y.idParametroRef from matriz_y y inner join amostra a on (a.idAmostra = y.idAmostra) where a.idAmostra = " + str(amostra) + "  order by y.idAmostra asc")

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


    def selectMatrizyYNOVO(self, idModelo):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            matrizY = []

            c.execute("select y.idamostratestes from amostratestes y where y.idamostratestes > 10 order by y.idamostratestes asc")

            listaAmostras = []
            for regAmostras in c:
                listaAmostras.append(regAmostras[0])


            print(listaAmostras)

            for amostra in listaAmostras:
                #print(amostra)
                linhaMatriz = []
                print("entrou")

                c.execute("select y.idamostratestes, y.vlResultado from amostratestes y  where y.idamostratestes = " + str(amostra) + "  order by y.idamostratestes asc")

                for regDadosAmostra in c:
                    linhaMatriz.append(regDadosAmostra[1])
                print(amostra)
                print(linhaMatriz)
                matrizY += [linhaMatriz]


            print(matrizY)

            c.close()

            return matrizY
        except Exception:
            print(Exception)
            return "Ocorreu um erro na busca dos dados"