import regression
import datasets
import numpy as np

import datasets
X, Y = datasets.load_linear_example1()

print("Xの中身:")
print(X)
print("Yの中身:")
print(Y)

model = regression.LinearRegression()
print(model.x)
model = regression.LinearRegression()
model.fit(X, Y)
prediction = model.predict(X)

print(prediction)

# データを準備
X, Y = datasets.load_linear_example1()

# モデルを学習
model = regression.LinearRegression()
model.fit(X, Y)

# スコア（ズレの合計）を表示
print(model.score(X, Y))