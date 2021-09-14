import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

H = lambda x: np.heaviside(x, 0)

x = np.linspace(-5, 5, 10000)

def Hs(x, alpha=1):
    return np.tanh(np.log(1 + np.exp(alpha * x)))

plt.plot(x, H(x), label="heaviside step")
for alpha in [1, 1.5, 2, 4, 8]:
    plt.plot(x, Hs(x, alpha), label=f"Heaviside step smooth,$\\alpha={alpha}$")
plt.legend(loc="upper left")
plt.title("$H_s(x) = \\tanh(\ln(1 + e^{\\alpha x}))$")
plt.show()

