import psycopg2

class Connect:

    #atributo global para ser
    #usado no modelo
    global cur
    global conexao

    #método construtor
    def __init__(self):
        #conexão com banco de dados
        try:
            conn = psycopg2.connect("\
                    dbname='MESTRADO'\
                    user='postgres'\
                    host='localhost'\
                    password='postgres'\
            ")

            self.cur = conn.cursor
            self.conexao = conn
        except:
            print ('Erro ao se conectar a base de dados!')

    #método destrutor
    def __del__(self):
        print ('Conexão finalizada!')
        del self;

    #método destrutor
    def retornaConexao(self):
        return self.conexao


