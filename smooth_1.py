import numpy as np
import matplotlib.pyplot as plt

H = lambda x: np.heaviside(x, 0)

x = np.linspace(-5, 5, 10000)

def Hs(x, alpha=1):
    return 0.5 + 0.5 * alpha * x / np.log(np.exp(alpha * x) + np.exp(-alpha * x))

plt.plot(x, H(x), label="heaviside step")
for alpha in [0.3, 0.5, 1, 2, 4, 8]:
    plt.plot(x, Hs(x, alpha), label=f"Heaviside step smooth, $\\alpha={alpha}$")
plt.legend(loc="upper left")
plt.title("$H_s(x) = \\frac{1}{2} + \\frac{\\alpha x}{2\log(e^{-\\alpha x}+e^{\\alpha x})}$")
plt.show()
