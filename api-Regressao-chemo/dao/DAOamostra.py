import sys

sys.path.append("..\dao")

from banco import Banco

class Amostra(object):

    def __init__(self, idAmostra=0, dtColetaAmostra="", tpAmostra="", dsObservacoes="", idModelo=0):
        self.info = {}
        self.idAmostra = idAmostra
        self.dtColetaAmostra = dtColetaAmostra
        self.tpAmostra = tpAmostra
        self.dsObservacoes = dsObservacoes
        self.idModelo = idModelo


    def insert(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute(
                "insert into amostra (idAmostra, dtColetaAmostra, tpAmostra, dsObservacoes, idModelo) values ( " +self.idAmostra+ ",'" + self.dtColetaAmostra + "', '" + self.tpAmostra + "', '" + self.dsObservacoes + "', '" + self.idModelo + "' )")

            banco.conexao.commit()
            c.close()

            return "Amostra cadastrada com sucesso!"
        except:
            return "Ocorreu um erro na inserção da Amostra"

    def update(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute(
                "update amostra set dtColetaAmostra = '" + self.dtColetaAmostra + "', tpAmostra = '" + self.tpAmostra + "', dsObservacoes = '" + self.dsObservacoes + "', idModelo = '" + self.idModelo + "' where idAmostra = " + self.idAmostra + " ")

            banco.conexao.commit()
            c.close()

            return "Amostra atualizada com sucesso!"
        except:
            return "Ocorreu um erro na alteração da amostra"

    def delete(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from amostra where idAmostra = " + self.idAmostra + " ")

            banco.conexao.commit()
            c.close()

            return "Amostra excluída com sucesso!"
        except:
            return "Ocorreu um erro na exclusão da Amostra"

    def select(self, idAmostra):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select idAmostra, dtColetaAmostra, tpAmostra, dsObservacoes, idModelo from amostra where idAmostra = " + idAmostra + "  ")

            for linha in c:
                self.idAmostra = linha[0]
                self.dtColetaAmostra = linha[1]
                self.tpAmostra = linha[2]
                self.dsObservacoes = linha[3]
                self.idModelo = linha[4]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca da Amostra"