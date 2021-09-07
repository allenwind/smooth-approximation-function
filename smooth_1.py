import numpy as np
import matplotlib.pyplot as plt

H = lambda x: np.heaviside(x, 0)

x = np.linspace(-5, 5, 10000)

def Hs(x, alpha=1):
    return 0.5 + 0.5 * alpha * x / np.log(np.exp(alpha * x) + np.exp(-alpha * x))

plt.plot(x, H(x), label="heaviside step")
plt.plot(x, Hs(x), label="Heaviside step smooth")
plt.legend(loc="upper left")
plt.show()
