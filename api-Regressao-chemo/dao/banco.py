from sqlalchemy import create_engine



class Banco():

    def __init__(self):
        try:
            print("Inicio de Conexao")
            db_string = "postgresql://postgres:postgres@localhost:5432/Quimiometria"

            db = create_engine(db_string)

            self.cur = db.cursor
            self.conexao = db
        except Exception:
            print(Exception)
