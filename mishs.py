import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 10000)
H = lambda x: np.heaviside(x, 0)

plt.plot(x, x * H(x), label="relu")
plt.plot(x, x * np.tanh(np.maximum(x, 0)), label="$x\\tanh(\max\{0, x \})$")
plt.plot(x, x * np.tanh(np.log(1 + np.exp(x))), label="mish(x)")
plt.legend(loc="upper left")
plt.show()
