import numpy as np
import matplotlib.pyplot as plt

H = lambda x: np.heaviside(x, 0)

x = np.linspace(-5, 5, 10000)

def Hs_f(x, alpha=1):
    """错误的构造实例"""
    return 0.5 * (1 + 1 / np.tanh(alpha * x))

def Hs(x, alpha=1):
    return alpha * x * (1 + np.tanh(alpha * x)) / (2 * np.log(np.exp(alpha * x) + np.exp(-alpha * x)))

plt.plot(x, H(x), label="heaviside step")
for alpha in [0.3, 0.5, 1, 2, 4]:
    plt.plot(x, Hs(x, alpha), label="Heaviside step smooth")
plt.legend(loc="upper left")
plt.show()
