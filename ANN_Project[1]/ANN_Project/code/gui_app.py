import tkinter as tk
from tkinter import ttk
import json
import numpy as np
from ann_core import PerceptronANN, WidrowHoffANN

# Load character data from the JSON file
with open("../data/character_data.json", "r") as letters:
    character_data = json.load(letters)

characters = list(character_data.keys())

# Defining X = character data, y_dict = character list,  y = add character data to y list
X = []
for char in characters:
    X.append(character_data[char])
y_dict = {}
for i, char in enumerate(characters):
    y_dict[char] = i
y = []
for char in characters:
    y.append(y_dict[char])

class ANNWrapper:
    def __init__(self, algo, input_size, learning_rate, epochs=100):
        self.algos = {}
        self.chars = characters
        # Train a separate model for each character
        for idx, char in enumerate(self.chars):
            model = algo(input_size, learning_rate, epochs)  # Initialize the model (Perceptron or Widrow-Hoff)
            # Create binary labels for each character (1 for current char, 0 for others)
            binary_labels = [1 if i == idx else 0 for i in range(len(self.chars))]
            model.train(X, binary_labels)  # Train the model
            self.algos[char] = model  # Store the trained model for the character

    def predict(self, sample):
        for char, model in self.algos.items():
            if model.predict(sample) == 1:
                return char
        return "Unknown"

# GUI class to build the application interface
class ANNApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ANN Character Classifier")

        # Initialize 5x5 grid of checkboxes
        self.matrix = [[tk.IntVar() for _ in range(5)] for _ in range(5)]
        self.learning_rate = tk.DoubleVar(value=0.1)  # Default learning rate is set to 0.1
        self.algorithm = tk.StringVar(value="Perceptron")  # Perceptron is used as default algorithm

        # Frame for algorithm selection and learning rate
        algo_frame = ttk.Frame(root)
        algo_frame.pack(pady=10)
        ttk.Label(algo_frame, text="Algorithm:").grid(row=0, column=0)
        algo_menu = ttk.Combobox(algo_frame, textvariable=self.algorithm, values=["Perceptron", "WidrowHoff"])
        algo_menu.grid(row=0, column=1)

        ttk.Label(algo_frame, text="Learning Rate:").grid(row=1, column=0)
        ttk.Entry(algo_frame, textvariable=self.learning_rate).grid(row=1, column=1)

        # Application base for the 5x5 grid of checkboxes (for character input)
        grid_frame = ttk.Frame(root)
        grid_frame.pack(pady=10)
        for i in range(5):
            for j in range(5):
                chk = tk.Checkbutton(grid_frame, variable=self.matrix[i][j])  # Checkbox for each grid cell
                chk.grid(row=i, column=j)

        # Button to evaluate the character
        ttk.Button(root, text="Classify", command=self.classify).pack(pady=10)

        # Label to show the classification result
        self.result_label = ttk.Label(root, text="Result: ")
        self.result_label.pack()

    # Classify the character by collecting the input and predicting
    def classify(self):
        # Collect the matrix values (5x5) as the input
        sample = [self.matrix[i][j].get() for i in range(5) for j in range(5)]
        algo = self.algorithm.get()  # Get the selected algorithm
        lr = self.learning_rate.get()  # Get the learning rate

        # Model selection
        if algo == "Perceptron":
            model = ANNWrapper(PerceptronANN, 25, lr)
        else:
            model = ANNWrapper(WidrowHoffANN, 25, lr)

        # Predicting and displaying the characters
        result = model.predict(sample)
        self.result_label.config(text=f"Result: {result}")

# Starting the program
if __name__ == "__main__":
    root = tk.Tk()
    app = ANNApp(root)
    root.mainloop()