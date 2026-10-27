
# utils.py

import numpy as np


class SingleLinearRegression:
    """Define uma regressão linear single simples"""

    def __init__(self, b0=0, b1=0):
        self.b0 = b0
        self.b1 = b1

    def predict(self, X):
        return self.b0 + self.b1 * X


class MSE:
    """Calcula o erro quadrático médio entre valores reais e previstos."""

    def calculate(self, y, y_pred):
        return np.mean((y - y_pred) ** 2)


class GradientDescent:
    """Otimiza os parâmetros da regressão usando o gradiente descendente."""

    def fit(self, model, X, y, learning_rate=0.01, epochs=1000):

        for _ in range(epochs):
            y_pred = model.predict(X)
            errors = y_pred - y

            # Derivadas parciais do MSE em relação aos parâmetros. (já derivados)
            db0 = 2 * np.mean(errors)
            db1 = 2 * np.mean(errors * X)

            model.b0 -= learning_rate * db0
            model.b1 -= learning_rate * db1

        return model


class OLS:
    """Estima os parâmetros da regressão pelo método dos mínimos quadrados."""

    def fit(self, model, X, y):
        x_mean = np.mean(X)
        y_mean = np.mean(y)

        b1 = np.sum((X - x_mean) * (y - y_mean)) / np.sum((X - x_mean) ** 2)

        b0 = y_mean - b1 * x_mean

        model.b0 = b0
        model.b1 = b1

        return model
