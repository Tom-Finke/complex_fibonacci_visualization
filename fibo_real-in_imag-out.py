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
    y.append(fibo.imag)

ax.set_xlabel('realer Input')
ax.set_ylabel('imaginärer Ouput')

ax.plot(x, y, linewidth=3)
ax.tick_params(axis='x', labelsize=15, pad=10)
ax.tick_params(axis='y', labelsize=15, pad=20)

# Besondere punkte zeichnen
for i in [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [4.5, fib(4.5).imag]]:
    plt.plot(i[0], i[1], 'ro', linewidth=100)  # Roten Punkt zeichnen

# Für ausgesuchte Punkte Linien bis zur Achese zeichnen
for i in [[4.5, round(fib(4.5).imag, 3), "red"]]:
    plt.plot([0, i[0]], [i[1], i[1]],
             linestyle="dotted", linewidth=2, color=i[2])
    plt.plot([i[0], i[0]], [0, i[1]],
             linestyle="dotted", linewidth=2, color=i[2])

    ax.annotate(f"({i[0]}|{i[1]}...)", (i[0] + 0.04, i[1] - 0.03),
                backgroundcolor="w", fontsize=15)


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
