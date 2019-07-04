import psycopg2



class Banco():

    def __init__(self):
        try:
            print("Inicio de Conexao")
            conn = psycopg2.connect("\
                           dbname='Quimiometria'\
                           user='postgres'\
                           host='localhost'\
                           password='postgres'\
                   ")
            print("Fim de Conexao")
            self.cur = conn.cursor
            self.conexao = conn
        except Exception:
            print(Exception)
