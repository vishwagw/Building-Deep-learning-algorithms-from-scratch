import numpy as np
import tensorflow as tf
from tensorflow.example.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) # y-labels are oh-encoded
