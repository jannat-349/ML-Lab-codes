# -*- coding: utf-8 -*-
"""Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ppArxy89UdbqEL9_QNCa7aGEzjlD3yIm
"""

class LinearRegression:
    def __init__(self):
        pass

    def fit(self, height, weight):
        self.x, self.y = height, weight
        self.m, self.b = 0, 0
        self.x_bar, self.y_bar = sum(self.x) / len(self.x), sum(self.y) / len(self.y)
        n = len(self.x)

        upper_value = sum((x - self.x_bar) * (y - self.y_bar) for x, y in zip(self.x, self.y))
        lower_value = sum((x - self.x_bar) ** 2 for x in self.x)

        self.m = upper_value / lower_value
        self.b = self.y_bar - (self.m * self.x_bar)


    def evaluate(self):
      MSE = sum((y - self.predict(x)) * (y - self.predict(x)) for x, y in zip(self.x, self.y))
      return MSE / len(self.x)


    def predict(self, x_value):
        y_value = self.m * x_value + self.b
        return y_value

heights = [165, 172, 158, 178, 155, 180, 162, 175, 168, 185]
weights = [60, 68, 52, 75, 50, 80, 55, 70, 65, 90]

model = LinearRegression()
model.fit(heights, weights)

print("Mean Square Error: ", model.evaluate())

test_heights = [170, 160, 175, 185, 155, 178, 162, 168, 182, 150, 190]

# Predict weights for each height in the test set
for height in test_heights:
    predicted_weight = model.predict(height)
    print(f"For height = {height}, predicted weight: {predicted_weight:.2f} kg")