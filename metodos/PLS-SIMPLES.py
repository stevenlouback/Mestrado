from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import r2_score

#X = [[0., 0., 1.], [1.,0.,0.], [2.,2.,2.], [2.,5.,4.]]
#Y = [[0.1, -0.2], [0.9, 1.1], [6.2, 5.9], [11.9, 12.3]]
X = [[1.65, 1, 66], [1.68, 1, 75], [1.91, 1, 100], [1.69, 1, 69]]
Y = [[26], [34], [30], [23]]
amostra = [[1.67, 1, 67]]

pls2 = PLSRegression(copy=True, max_iter=500, n_components=1, scale=True, tol=1e-06)
pls2.fit(X, Y)

Y_pred = pls2.predict(amostra)

print(Y_pred)

print(r2_score(pls2.predict(X), Y))
