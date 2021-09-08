import numpy as np
import matplotlib.pyplot as plt

H = lambda x: np.heaviside(x, 0)

x = np.linspace(-5, 5, 10000)

def Hs(x, alpha=1):
    return 0.5 * (1 + (alpha * x) / (1 + (alpha * x) ** 2) ** (1 / 2))

plt.plot(x, H(x), label="heaviside step")
for alpha in [0.5, 1, 2, 4, 8]:
    plt.plot(x, Hs(x, alpha), label=f"Heaviside step smooth, $\\alpha={alpha}$")
plt.legend(loc="upper left")
plt.title("$H_s(x) = \\frac{1}{2}[1 + \\frac{\\alpha x}{(1 + \\alpha^2 x^{2} )^{\\frac{1}{2}}} ]$")
plt.show()
