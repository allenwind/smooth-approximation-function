import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 10000)

def approx_delta(x, sigma):
    return 1 / np.sqrt(np.pi * sigma ** 2) * np.exp(- (x / sigma) ** 2)

for sigma in np.linspace(0.5, 0.1, 10):
    plt.plot(x, approx_delta(x, sigma), label=f"$\\alpha={sigma:.2f}$")
plt.legend(loc="upper left")
plt.title("$\\frac{1}{\sqrt{\pi \sigma^2}}e^{-(x/\sigma)^{2}}$")
plt.show()
