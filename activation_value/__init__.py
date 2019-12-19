import math


def sigmoid_function(z):
    return float(1 / (1 + math.exp(-z)))


def tanh_function(z):
    return float((math.exp(z) - math.exp(-z)) / (math.exp(-z) + math.exp(z)))


def relu(z):
    return max(0.0, z)


print(tanh_function(10))
