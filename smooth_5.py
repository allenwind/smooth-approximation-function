import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

H = lambda x: np.heaviside(x, 0)

x = np.linspace(-5, 5, 10000)

def Hs(x, sigma=0.5):
    return 0.5 * (1 + erf(x / (sigma * np.sqrt(2))))

plt.plot(x, H(x), label="heaviside step")
for sigma in [1, 0.5, 0.2, 0.1, 0.01]:
    plt.plot(x, Hs(x, sigma), label=f"Heaviside step smooth, $\sigma={sigma}$")
plt.legend(loc="upper left")
plt.title("$H_s(x) = \\frac {1}{2}\left[1+\operatorname {erf} \left({\\frac {x }{\sigma {\sqrt {2}}}}\\right)\\right]$")
plt.show()
