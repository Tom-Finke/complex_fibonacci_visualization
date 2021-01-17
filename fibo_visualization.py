import matplotlib.pyplot as plt
import matplotlib as mpl
import math
import numpy as np
from mpl_toolkits.axisartist.axislines import SubplotZero
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as mticker


def draw(graphs: list, stepsize: float = 0.001, axes={"x": {"name": "Re(z)"}, "y": {
         "name": "Im(z)"}, },
         linewidth: int = 3, points: list = []):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    x, y = [], []
    three_dimensional = False
    three_dimensional = True if True in [
        True for graph in graphs if "z_out" in graph] else False
    print(three_dimensional)
    if(three_dimensional):
        z = []
        ax = fig.gca(projection='3d')
        ax.set_zlabel(axes[z]["name"]
                      if "z" in axes and "name" in axes["z"] else "z")

    ax.set_xlabel(
        axes["x"]["name"] if "x" in axes and "name" in axes["x"] else "x", fontsize=15)
    ax.xaxis.set_label_coords(1, 0.45)
    ax.set_ylabel(axes["y"]["name"] if "y" in axes and "name" in axes["y"] else "y",
                  rotation='horizontal', fontsize=15)
    ax.yaxis.set_label_coords(0.5, 1.02)
    if("x" in axes and "format" in axes["x"]):
        plt.gca().xaxis.set_major_formatter(
            mticker.FormatStrFormatter(axes["x"]["format"]))
    if("y" in axes and "format" in axes["y"]):
        plt.gca().yaxis.set_major_formatter(
            mticker.FormatStrFormatter(axes["y"]["format"]))
    if("z" in axes and "format" in axes["z"] and three_dimensional):
        plt.gca().zaxis.set_major_formatter(
            mticker.FormatStrFormatter(axes["z"]["format"]))

    ax.tick_params(axis='x', labelsize=15, pad=10)
    ax.tick_params(axis='y', labelsize=15, pad=20)
    # Koordinatensystem anpassen --> 2 Achsen die sich in Ursprung treffen
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    if(not three_dimensional):
        ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
                transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot((0), (1), ls="", marker="^", ms=10, color="k",
                transform=ax.get_xaxis_transform(), clip_on=False)

    for graph in graphs:
        x, y, z = [], [], []
        for i in range(
                int(graph["interval"][0] * (1 / stepsize)),
                int(graph["interval"][1] * (1 / stepsize))):
            i *= stepsize
            x.append(graph["x_out"](i))
            y.append(graph["y_out"](i))

            z.append(graph["z_out"](
                i) if "z_out" in graph else 0) if three_dimensional else 0  # Die z-achse wird nur befüllt, wenn einer der Grapghen 3-Dimensional ist
        print("calculated")
        if(three_dimensional):
            ax.scatter(x, y, z, s=linewidth, zorder=1, color=graph["color"])
        else:
            ax.plot(x, y, linewidth=linewidth, color=graph["color"])

    for point in points:
        x = int(point["x"]) if round(point["x"], 1) == int(
            point["x"]) else point["x"]
        y = int(point["y"]) if round(point["y"], 1) == int(
            point["y"]) else point["y"]
        z = (int(point["z"]) if round(point["z"], 1) == int(
            point["z"]) else point["z"]) if "z" in point else 0
        print(z)
        if(three_dimensional):
            ax.scatter(x, y, z, s=linewidth * 2,
                       zorder=3, color=point["color"] if "color" in point else "C0")
        else:
            ax.plot(x, y, color=point["color"] if "color" in point else "C0", marker="o",
                    linewidth=linewidth * 2)

        if("annotation" in point and point["annotation"] == True):

            # Ergebnisse mit mehr als 3 Nachkommastellen werden zur Darstellung gerundet
            annotation = y if round(y, 3) == y else str(round(y, 3)) + "..."
            ax.annotate(f"({x}|{annotation})",
                        (x + 0.06, y - 0.5), fontsize=15)
        if("lines" in point and point["lines"] == True):

            plt.plot([0, x], [y, y],
                     linestyle="dotted", linewidth=2, color=point["color"] if "color" in point else "C0")
            plt.plot([x, x], [0, y],
                     linestyle="dotted", linewidth=2, color=point["color"] if "color" in point else "C0")
    plt.show()


golden_ratio = (1 + math.sqrt(5)) / 2


def binet(n):
    return complex((golden_ratio**n - (1 / -golden_ratio)**n) / math.sqrt(5))


draw(graphs=[{"interval": [0, 5.7], "x_out": lambda x: binet(x).real, "y_out": lambda x: binet(x).imag, "color": "b"}
             ],
     stepsize=0.01,
     axes={"x": {"name": "Re(z)"}, "y": {
         "name": "Im(z)", "format": '%.1fi'}, },
     points=[
    {"x": binet(x).real, "y": binet(x).imag, "color": "red",
     "lines": False, "annotation": False} for x in range(0, 6)
])
