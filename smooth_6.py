import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

H = lambda x: np.heaviside(x, 0)

x = np.linspace(-5, 5, 10000)

def Hs(x, gamma=0.1):
    return 0.5 + np.arctan(x / gamma) / np.pi

plt.plot(x, H(x), label="heaviside step")
for gamma in [1, 0.5, 0.2, 0.1, 0.01]:
    plt.plot(x, Hs(x, gamma), label=f"Heaviside step smooth,$\gamma={gamma}$")
plt.legend(loc="upper left")
plt.title("$H_s(x) = \\frac{1}{2} + \\frac{\\arctan(x)}{\pi}$")
plt.show()

