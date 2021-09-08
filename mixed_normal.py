import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def gen_mixed_normal(x, n=10):
    y = 0
    ws = np.random.uniform(0, 1, n)
    ws = ws / np.sum(ws)
    for i in range(n):
        u = np.random.uniform(-5, 5)
        sigma = np.random.uniform(0.5, 1.5)
        y += stats.norm.pdf(x, u, sigma) * ws[i]
    return y

x = np.linspace(-5, 5, 10000)
for i in range(5):
    y = gen_mixed_normal(x)
    plt.plot(x, y)
plt.show()
