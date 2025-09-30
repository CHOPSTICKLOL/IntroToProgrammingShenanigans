
import numpy as np

class PerceptronANN:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = np.zeros(input_size + 1)  # +1 for bias

    def activation(self, x):
        return 1 if x >= 0 else 0

    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                xi = np.insert(xi, 0, 1)
                prediction = self.activation(np.dot(self.weights, xi))
                error = target - prediction
                self.weights += self.lr * error * xi

    def predict(self, x):
        x = np.insert(x, 0, 1)
        return self.activation(np.dot(self.weights, x))


class WidrowHoffANN:
    def __init__(self, input_size, learning_rate=0.01, epochs=100):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = np.zeros(input_size + 1)

    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                xi = np.insert(xi, 0, 1)
                output = np.dot(self.weights, xi)
                error = target - output
                self.weights += self.lr * error * xi

    def predict(self, x):
        x = np.insert(x, 0, 1)
        return 1 if np.dot(self.weights, x) >= 0.5 else 0
