# simple mathematical question for understanding:
import numpy as np

inputs = [1,2,3, 2.5]

# weights:
weights = [[0.2, 0.8, - 0.5, 1],
           [0.5, - 0.91, 0.26, - 0.5],
           [ - 0.26, - 0.27, 0.17, 0.87]]

# baises:
biases = [2,3,0.5]

outputs = np.dot(weights, inputs) + biases

# Or Use this method
# np.dot(inputs, weights.T) + biases

# printing results
print(outputs)