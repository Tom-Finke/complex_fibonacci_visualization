import matplotlib.pyplot as plt
import math
import numpy as np
from mpl_toolkits.axisartist.axislines import SubplotZero
golden_ratio = (1 + math.sqrt(5)) / 2


def fib(n):
    return complex((golden_ratio**n - (1 / -golden_ratio)**n) / math.sqrt(5))


fig = plt.figure()

ax = fig.add_subplot(111)
x, y = [], []


for i in np.arange(0.0, 6.7, 0.001):
    i = float(i)
    print(i)
    fibo = fib(i)
    x.append(i)
    y.append(fibo.real)

ax.set_xlabel('realer Input')
ax.set_ylabel('realer Ouput')

ax.plot(x, y, linewidth=3)
ax.tick_params(axis='x', labelsize=15, pad=10)
ax.tick_params(axis='y', labelsize=15, pad=20)

# Besondere punkte zeichnen
for i in [[1, 1], [2, 1], [3, 2], [4, 3], [5, 5], [6, 8], [4.5, fib(4.5).real]]:
    plt.plot(i[0], i[1], 'ro', linewidth=100)  # Roten Punkt zeichnen
    ax.annotate(f"({i[0]}|{i[1]})", (i[0] + 0.06, i[1] - 0.5),
                backgroundcolor="w", fontsize=15)

# Für ausgesuchte Punkte Linien bis zur Achese zeichnen
for i in [[3, 2, "red"], [4.5, fib(4.5).real, "red"]]:
    plt.plot([0, i[0]], [i[1], i[1]],
             linestyle="dotted", linewidth=2, color=i[2])
    plt.plot([i[0], i[0]], [0, i[1]],
             linestyle="dotted", linewidth=2, color=i[2])


ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
        transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot((0), (1), ls="", marker="^", ms=10, color="k",
        transform=ax.get_xaxis_transform(), clip_on=False)
plt.show()
