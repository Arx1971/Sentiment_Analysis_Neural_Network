import numpy as np


def sigmoid_function(z):
    return float(1 / (1 + np.exp(-z)))


def tanh_function(z):
    return float((np.exp(z) - np.exp(-z)) / (np.exp(-z) + np.exp(z)))


def relu(z):
    return max(0.0, z)
