import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
columns = [
    'symboling', 'normalized-losses', 'make', 'fuel-type',
    'aspiration', 'num-of-doors', 'body-style', 'drive-wheels',
    'engine-location', 'wheel-base', 'length', 'width',
    'height', 'curb-weight', 'engine-type', 'num-of-cylinders',
    'engine-size', 'fuel-system', 'bore', 'stroke',
    'compression-ratio', 'horsepower', 'peak-rpm',
    'city-mpg', 'highway-mpg', 'price'
]

df = pd.read_csv(url, names=columns, na_values='?')

poly = PolynomialFeatures(degree=11)
df_poly = df.dropna(subset=['highway-mpg', 'price'])
X_poly = poly.fit_transform(df_poly[['highway-mpg']])
Y = df_poly['price']

poly_model = LinearRegression()
poly_model.fit(X_poly, Y)

print("Polynomial R²:", poly_model.score(X_poly, Y))
Y_pred_poly = poly_model.predict(X_poly)

print("Polynomial MSE:", mean_squared_error(Y, Y_pred_poly))

df_mlr = df.dropna(subset=['normalized-losses', 'highway-mpg', 'price'])
print(df[['normalized-losses', 'highway-mpg', 'price']].isna().sum())
print(df[['engine-size', 'price']].head())

df = df.dropna(subset=['price'])
print(df[['engine-size', 'price']].isna().sum())
lm = LinearRegression()

X = df[['engine-size']]
Y = df['price']

lm.fit(X, Y)

print("R²:", lm.score(X, Y))

Y_pred = lm.predict(X)
print("MSE:", mean_squared_error(Y, Y_pred))
print("Модель успешно обучена!")

plt.figure(figsize=(12, 10))
sns.residplot(x=df['engine-size'], y=df['price'])
plt.show()

print(df[['normalized-losses', 'highway-mpg', 'price']].isna().sum())

lm2 = LinearRegression()

X = df_mlr[['normalized-losses', 'highway-mpg']]
Y = df_mlr['price']

lm2.fit(X, Y)

print("MLR R²:", lm2.score(X, Y))

Y_pred_mlr = lm2.predict(X)
print("MLR MSE:", mean_squared_error(Y, Y_pred_mlr))

plt.figure(figsize=(10, 6))

plt.scatter(
    df_poly['highway-mpg'],
    df_poly['price'],
    label='Реальні дані'
)

sort_idx = df_poly['highway-mpg'].argsort()
X_sorted = df_poly[['highway-mpg']].iloc[sort_idx]
X_poly_sorted = poly.transform(X_sorted)

plt.plot(
    X_sorted['highway-mpg'],
    poly_model.predict(X_poly_sorted),
    color='red',
    label='Полі-модель'
)

plt.xlabel('Highway MPG')
plt.ylabel('Price')
plt.title('Polynomial Regression')
plt.legend()
plt.show()

for degree in [2, 3, 5, 11]:
    poly_test = PolynomialFeatures(degree=degree)
    X_test = poly_test.fit_transform(df_poly[['highway-mpg']])

    model_test = LinearRegression()
    model_test.fit(X_test, df_poly['price'])

    print(f"Ступінь {degree}, R²: {model_test.score(X_test, df_poly['price']):.3f}")