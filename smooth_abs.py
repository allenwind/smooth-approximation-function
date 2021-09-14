import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 10000)

fabs = lambda x: np.abs(x)

def fabs1(x, alpha=1):
    return np.log(np.exp(alpha * x) + np.exp(-alpha * x)) / alpha

def fabs2(x, mu=0.1):
    return np.sqrt(x ** 2 + mu / (np.exp(x) + np.exp(-x)))

def fabs3(x, eps=0.1):
    return x ** 2 / np.sqrt(x ** 2 + eps ** 2)

def fabs4(x, alpha=1):
    return alpha * x ** 2 / np.log(np.exp(alpha * x) + np.exp(-alpha * x))

def fabs5(x, alpha=1):
    return x * np.tanh(alpha * x)

def fabs6(x, alpha=1):
    return x * erf(x / (alpha * np.sqrt(2)))

plt.plot(x, fabs(x), label="abs")
for i in range(1, 7):
    func = vars()[f"fabs{i}"]
    plt.plot(x, func(x), label=f"abs smooth {i}")
plt.legend(loc="upper left")
plt.show()
