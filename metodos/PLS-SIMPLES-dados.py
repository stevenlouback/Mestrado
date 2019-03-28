import sys

sys.path.append("..\dao")

from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import r2_score

from DAOmatrizy import Matrizy
from DAOmatrizx import Matrizx

matrizX = Matrizx()
matrizY = Matrizy()

idModelo = 1

idAmostraTestes = 97

Y = matrizY.selectMatrizyYNOVO(idModelo)

X = matrizX.selectMatrizXModeloNOVO(idModelo)

amostraPredicao = matrizX.selectAmostra(idAmostraTestes)

pls2 = PLSRegression(copy=True, max_iter=5000, n_components=10, scale=True, tol=1e-06)

pls2.fit(X, Y)

# Get X scores
T = pls2.x_scores_

# Get X loadings
P = pls2.x_loadings_

Y_pred = pls2.predict(amostraPredicao)

print('Valor Predito:')
print(Y_pred)

print('R2 do modelo PLS')
print(pls2.score(X,Y,sample_weight=None))


#print('R2 do modelo')
#print(r2_score(pls2.predict(X), Y))
