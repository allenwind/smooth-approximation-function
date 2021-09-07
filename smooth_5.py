import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

H = lambda x: np.heaviside(x, 0)

x = np.linspace(-5, 5, 10000)

def Hs(x, sigma=0.5):
    return 0.5 * (1 + erf(x / (sigma * np.sqrt(2))))

plt.plot(x, H(x), label="heaviside step")
plt.plot(x, Hs(x), label="Heaviside step smooth")
plt.legend(loc="upper left")
plt.show()

