import psycopg2

class Banco():

    def __init__(self):
        try:
            conn = psycopg2.connect("\
                           dbname='QUIMIOMETRIA'\
                           user='postgres'\
                           host='127.0.0.1'\
                           password='postgres'\
                   ")

            self.cur = conn.cursor
            self.conexao = conn
        except:
            print('Erro ao se conectar a base de dados!')