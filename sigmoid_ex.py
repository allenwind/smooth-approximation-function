import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 10000)

def sigmoid(x, alpha=0, beta=1):
    return (np.exp(x) + alpha) / (np.exp(x) + beta)

H = lambda x: np.heaviside(x, 0)
plt.plot(x, H(x), label="heaviside step")
for alpha in [0, 0.2, 0.5, 0.8, 1]:
    for beta in [1, 1.5, 2, 2.5, 3, 4, 5]:
        y = sigmoid(x, alpha, beta)
        y = (beta * y - alpha) / (beta - alpha)
        plt.plot(x, y, label=f"$\\alpha={alpha}, \\beta={beta}$")
plt.legend(loc="upper right")
plt.show()
