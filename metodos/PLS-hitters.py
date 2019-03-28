import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.cross_decomposition import PLSRegression
from sklearn.preprocessing import scale

# pandas==0.19.2, scikit-learn==0.18.1

pd.options.display.float_format = '{: .4f}'.format

rebatedores = pd.read_csv('../metodos/Hitters.csv', index_col=0)

rebatedores = rebatedores.dropna()

rebatedores = pd.get_dummies(rebatedores, drop_first=True)

rebatedores_train, hitters_test = train_test_split(rebatedores, test_size=0.5, random_state=1)
print(rebatedores_train)

rebatedores_train_p = rebatedores_train.drop('Salary', axis=1)

print(rebatedores_train_p)

rebatedores_test_p = hitters_test.drop('Salary', axis=1)

rebatedores_p = rebatedores.drop('Salary', axis=1)

kf = KFold(n_splits=10, random_state=1)
print('\n Components  MSE')

for i in range(1, 20):
    pls = PLSRegression(n_components=i)
    scores = cross_val_score(pls, scale(rebatedores_train_p),
                             rebatedores_train['Salary'],
                             scoring='neg_mean_squared_error',
                             cv=kf)
    print('%5d %10.0f' % (i, -scores.mean()))

pls = PLSRegression(n_components=2)
pls.fit(scale(rebatedores_train_p), rebatedores_train['Salary'])
mse = mean_squared_error(hitters_test['Salary'],
                         pls.predict(scale(rebatedores_test_p)))
print('MSE from test data: %.0f' % mse)