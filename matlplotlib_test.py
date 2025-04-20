# using matplotlib library for DNN:
import numpy as np
import matplotlib.pyplot as plt

# values:
a = np.array([0, 0, 1, 1])
b = np.array([0, 1, 0, 1])

# y_and = np.array([[0, 0, 0, 1]])
y_xor = np.array([[0,1,1,0]])

# combining for totol inputs:
total_input = []

total_input = [a, b]

total_input = np.array(total_input)
#print(total_input)
