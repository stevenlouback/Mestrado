
#importa a classe DAO PRINCIPAL
import daoPrincipal

print("\n Teste..\n")

#instância da classe do modelo
dao = daoPrincipal.Dao()

#Exemplo de Insert
#dao.executaSQL("INSERT INTO instrumento_coletor(idcoletor, dscoletor, dsinformacoes) VALUES (999,'AAAA','BBBB')")

#executa a consulta
rows = dao.consulta("SELECT * FROM instrumento_coletor")

#impressão dos result sets da query
import pprint
print('\n -- Lista de pessoas -- \n')
pprint.pprint(rows)

if __name__ == '__main__':
    print("Olá, esse sera um teste de conexão!")
