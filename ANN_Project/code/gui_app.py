
import tkinter as tk
from tkinter import ttk
import json
import numpy as np
from ann_core import PerceptronANN, WidrowHoffANN

with open("../data/character_data.json", "r") as f:
    character_data = json.load(f)

characters = list(character_data.keys())
X = np.array([character_data[ch] for ch in characters])
y_dict = {ch: i for i, ch in enumerate(characters)}
y = np.array([y_dict[ch] for ch in characters])

class ANNWrapper:
    def __init__(self, algo, input_size, learning_rate, epochs=100):
        self.algos = {}
        self.chars = characters
        for idx, char in enumerate(self.chars):
            model = algo(input_size, learning_rate, epochs)
            binary_labels = [1 if i == idx else 0 for i in range(len(self.chars))]
            model.train(X, binary_labels)
            self.algos[char] = model

    def predict(self, sample):
        for char, model in self.algos.items():
            if model.predict(sample) == 1:
                return char
        return "Unknown"

class ANNApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ANN Character Classifier")

        self.matrix = [[tk.IntVar() for _ in range(5)] for _ in range(5)]
        self.learning_rate = tk.DoubleVar(value=0.1)
        self.algorithm = tk.StringVar(value="Perceptron")

        algo_frame = ttk.Frame(root)
        algo_frame.pack(pady=10)
        ttk.Label(algo_frame, text="Algorithm:").grid(row=0, column=0)
        algo_menu = ttk.Combobox(algo_frame, textvariable=self.algorithm, values=["Perceptron", "WidrowHoff"])
        algo_menu.grid(row=0, column=1)

        ttk.Label(algo_frame, text="Learning Rate:").grid(row=1, column=0)
        ttk.Entry(algo_frame, textvariable=self.learning_rate).grid(row=1, column=1)

        grid_frame = ttk.Frame(root)
        grid_frame.pack(pady=10)
        for i in range(5):
            for j in range(5):
                chk = tk.Checkbutton(grid_frame, variable=self.matrix[i][j])
                chk.grid(row=i, column=j)

        ttk.Button(root, text="Classify", command=self.classify).pack(pady=10)
        self.result_label = ttk.Label(root, text="Result: ")
        self.result_label.pack()

    def classify(self):
        sample = [self.matrix[i][j].get() for i in range(5) for j in range(5)]
        algo = self.algorithm.get()
        lr = self.learning_rate.get()
        if algo == "Perceptron":
            model = ANNWrapper(PerceptronANN, 25, lr)
        else:
            model = ANNWrapper(WidrowHoffANN, 25, lr)
        result = model.predict(sample)
        self.result_label.config(text=f"Result: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ANNApp(root)
    root.mainloop()
