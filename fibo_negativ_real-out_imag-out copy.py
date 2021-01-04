import matplotlib.pyplot as plt
import math
import numpy as np
from mpl_toolkits.axisartist.axislines import SubplotZero
golden_ratio = (1 + math.sqrt(5)) / 2


def fib(n):
    return complex((golden_ratio**n - (1 / -golden_ratio)**n) / math.sqrt(5))


cnums, x, y = [], [], []
for i in np.arange(-6.7, 0, 0.001):
    i = float(i)
    print(i)
    cnums.append(fib(i))


fig = plt.figure()

# cnums = np.arange(5) + 1j * np.arange(6,11)
x = [x.real for x in cnums]
y = [x.imag for x in cnums]


ax = fig.add_subplot(111)
ax.plot(x, y, linewidth=3)
ax.tick_params(axis='x', labelsize=15, pad=10)
ax.tick_params(axis='y', labelsize=15, pad=20)

for i in [1, -1, 2, -3, 5, -8]:
    plt.plot(i, 0, 'ro', linewidth=100)  # Roten Punkt zeichnen
# ax.annotate(f"({i}|0)", (i, -0.03), backgroundcolor="w")


ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xlabel('reell out')
ax.set_ylabel('imag out')

ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
        transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot((0), (1), ls="", marker="^", ms=10, color="k",
        transform=ax.get_xaxis_transform(), clip_on=False)
plt.show()
