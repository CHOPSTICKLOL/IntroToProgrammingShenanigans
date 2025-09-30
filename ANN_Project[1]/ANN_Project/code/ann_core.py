import numpy as np

class PerceptronANN:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        # Initialize the perceptron with a learning rate, number of epochs, and weights (initial
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = np.zeros(input_size + 1)  # +1 for bias

    def activation(self, x):
        # Activation function: returns 1 if input >= 0, else returns 0
        return 1 if x >= 0 else 0

    def train(self, X, y):
        # Training loop for the perceptron
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                # Add the bias term (1) to the input vector (xi)
                xi = np.insert(xi, 0, 1)
                # Compute the prediction
                prediction = self.activation(np.dot(self.weights, xi))
                # Calculate the error (difference between target and prediction)
                error = target - prediction
                #update the weight
                self.weights += self.lr * error * xi

    def predict(self, x):
        # Insert bias and apply the activation function
        x = np.insert(x, 0, 1)
        return self.activation(np.dot(self.weights, x))


class WidrowHoffANN:
    # Initialize the Widrow-Hoff (Least Mean Squares) model
    def __init__(self, input_size, learning_rate=0.01, epochs=100):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = np.zeros(input_size + 1) # Initialize weights (including bias)

    def train(self, X, y):
        # Training loop for Widrow-Hoff ANN
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                xi = np.insert(xi, 0, 1) # Add bias term to the input
                output = np.dot(self.weights, xi)
                # Calculate error (difference between target and output)
                error = target - output
                # Update weights
                self.weights += self.lr * error * xi

    def predict(self, x):
        # Insert bias and check if the weighted sum is greater than 0.5
        x = np.insert(x, 0, 1)
        return 1 if np.dot(self.weights, x) >= 0.5 else 0
