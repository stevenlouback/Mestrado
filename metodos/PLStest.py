import numpy as np
import pandas as pd


from sklearn.cross_decomposition import PLSRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

train = pd.read_csv("../metodos/fashion-mnist_train.csv")
train = train[train.label.isin([6, 7])]
train = train.assign(label=(train.label == 6))

X = train.values[:, 1:]
y = train.values[:, :1]

pls = PLSRegression(n_components=4)

pls.fit(X, y)

y_pred = np.round(pls.predict(X)) == 6

test = pd.read_csv("../metodos/fashion-mnist_test.csv")
test = test[test.label.isin([6, 7])]
test = test.assign(label=(test.label == 6))

X_t = test.values[:, 1:]
y_t = test.values[:, :1]

#r2_score(pls.predict(X_t), y_t)
print(r2_score(pls.predict(X_t), y_t))

clf2 = LinearRegression()
clf2.fit(X, y)
y_pred = np.round(clf2.predict(X)) == 6

#r2_score(clf2.predict(X_t), y_t)
#r2_score(r2_score(clf2.predict(X_t), y_t))

#plt.style.use('fivethirtyeight')
#pd.Series((clf1.coef_.T - clf2.coef_).flatten()).plot.hist(bins=100)

