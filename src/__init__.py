if __name__ == '__main__':
    print('Olá, esse sera um teste de conexão!')

#importa a classe do modelo
import modelo

print('\n iniciando teste...\n')

#instância da classe do modelo
#e executa a query
teste = ModeloTeste()
rows = teste.query()

#impressão dos result sets da query
import pprint
print('\n -- Lista de pessoas -- \n')
pprint.pprint(rows)
