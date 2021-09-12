import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 10000)

H = lambda x: np.heaviside(x, 0)

def Hs1(x, alpha=1):
    return 0.5 + 0.5 * alpha * x / np.log(np.exp(alpha * x) + np.exp(-alpha * x))

def Hs2(x, alpha=1):
    return 0.5 * (1 + (alpha * x) / (1 + (alpha * x) ** 2) ** (1 / 2))

def Hs3(x, alpha=3):
    return (1 + np.exp(-alpha * x) + x * np.exp(-alpha * x)) / (1 + np.exp(-alpha * x)) ** 2

def Hs4(x, sigma=0.5):
    return 0.5 * (1 + erf(x / (sigma * np.sqrt(2))))

def Hs5(x, gamma=0.1):
    return 0.5 + np.arctan(x / gamma) / np.pi

plt.plot(x, x * H(x), label="heaviside step")
for i in range(1, 6):
    func = vars()[f"Hs{i}"]
    plt.plot(x, x * func(x), label=f"Heaviside step smooth {i}")
plt.legend(loc="upper left")
plt.show()
