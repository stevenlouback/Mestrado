import sys
import numpy as np
import matplotlib.pyplot as plt


sys.path.append("..\dao")

from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import r2_score, mean_squared_error, median_absolute_error, mean_absolute_error, mean_squared_log_error, coverage_error, label_ranking_loss, explained_variance_score, label_ranking_average_precision_score

from DAOmatrizy import Matrizy
from DAOmatrizx import Matrizx

matrizX = Matrizx()
matrizY = Matrizy()

idModelo = 1

idAmostraTestes = 351

conjunto = "CALIBRA"

X = matrizX.selectMatrizXModeloNOVO(idModelo, conjunto)
Y = matrizY.selectMatrizyYNOVO(idModelo, conjunto)

amostraPredicao = matrizX.selectAmostra(idAmostraTestes)

pls = PLSRegression(copy=True, max_iter=500, n_components=12, scale=False, tol=1e-06)

pls.fit(X, Y)

#L = pls.x_loadings_
#S = pls.x_scores_

#pls.fit(S, Y)

Y_pred = pls.predict(amostraPredicao)

print('Amostra: ' + str(idAmostraTestes) +  ' - Valor Predito :' + str(Y_pred))

print('R2 do modelo PLS')
print(pls.score(X,Y,sample_weight=None))
print(r2_score(pls.predict(X),Y))

matYPred = []

for i in range(1, 349):
    print(i)
    linhaMatriz = []
    idAmostraTestes = i
    amostraPredicao = matrizX.selectAmostra(idAmostraTestes)
    Y_pred = pls.predict(amostraPredicao)
    print(Y_pred)
    linhaMatriz.append(np.double(Y_pred))
    matYPred += [linhaMatriz]

print('RMSEC')
#print(mean_squared_error(Y,matYPred))
raizQ = mean_squared_error(Y,matYPred) ** (1/2)
print(raizQ)


'''


print('Erro absoluto mediano')
print(median_absolute_error(Y,matYPred))

print('Erro quadrático log Médio')
print(mean_squared_log_error(Y,matYPred))

print('coverage_error ')
print(coverage_error(np.array(Y),np.array(pls.y_scores_)))

print('label_ranking_average_precision_score ')
print(label_ranking_average_precision_score(np.array(Y),np.array(pls.y_scores_)))

print('label_ranking_loss')
print(label_ranking_loss(np.array(Y),np.array(pls.y_scores_)))

print('explained_variance_score')
print(explained_variance_score(Y,matYPred))


'''


#print('R2 do modelo')
#print(r2_score(pls2.predict(X), Y))


