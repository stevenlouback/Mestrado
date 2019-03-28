from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np

# Define PLS object
pls = PLSRegression(n_components=5)

train = pd.read_csv("../metodos/fashion-mnist_train.csv")
train = train[train.label.isin([6, 7])]
train = train.assign(label=(train.label == 6))

X_calib = train.values[:, 1:]
Y_calib = train.values[:, :1]

#Fit
pls.fit(X_calib, Y_calib)

#Prediction  np.round - arrendonda o array para decimal
y_pred = np.round(pls.predict(X_calib)) == 2
print(y_pred)




test = pd.read_csv("../metodos/fashion-mnist_test.csv")
test = test[test.label.isin([6, 7])]
test = test.assign(label=(test.label == 6))

X_t = test.values[:, 1:]
y_t = test.values[:, :1]

#Y_pred = pls.predict(X_valid)

#Calculate scores
#score = r2_score(Y_valid, Y_pred)
#mse = mean_squared_error(Y_valid, Y_pred)