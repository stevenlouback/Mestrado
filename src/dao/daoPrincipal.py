#importa o módulo de conexão
import sys


sys.path.append("D:\Mestrado\Dissertacao\Mestrado\Mestrado\src\conexaoBanco")

import conexao as con


class Dao:

    global conn

    #método construtor
    def __init__(self):
        # instância da classe de conexão
        self.conn = con.Connect()


    #query para teste
    def consulta(self,sql):

        #usa o atributo de cursor da classe
        #de conexão para fazer a query
        qry = self.conn.cur()
        qry.execute(sql)
        return qry.fetchall()


    def executaSQL(self, sql):
        qry = self.conn.cur()
        qry.execute(sql)


    #método destrutor
    def __del__(self):
        del self

