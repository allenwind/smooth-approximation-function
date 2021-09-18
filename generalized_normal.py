import numpy as np
from scipy.special import gammainc
from scipy.special import gamma
from scipy.special import exp1
import matplotlib.pyplot as plt

def linc_gamma(x, s):
    """lower incomplete gamma function"""
    if s == 0:
        return exp1(x)
    else:
        return gamma(s) * gammainc(s, x)

def generalized_normal(x, alpha, beta):
    return 0.5 + np.sign(x) * linc_gamma(np.abs(x / alpha) ** beta, 1 / beta) / (2 * gamma(1 / beta))

x = np.linspace(-5, 5, 10000)

for i, alpha in enumerate([0.5, 1, 1.5, 2], start=1):
    plt.subplot(2, 2, i)
    for beta in [0.5, 0.8, 1, 1.5, 2, 3, 8]:
        y = generalized_normal(x, alpha, beta)
        plt.plot(x, y, label=f"$\\alpha={alpha},\\beta={beta}$")
    plt.legend(loc="upper left")
plt.suptitle("generalized normal distribution")
plt.show()
