import matplotlib.pyplot as plt
import matplotlib as mpl
import math
import numpy as np
from mpl_toolkits.axisartist.axislines import SubplotZero
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as mticker


def draw(graphs: list, stepsize: float = 0.001, axis={"x-name": "x", "y-name": "y"},
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
        ax.set_zlabel(axis["z-name"] if "z-name" in axis else "z")

    ax.set_xlabel(axis["x-name"] if "x-name" in axis else "x", fontsize=15)
    ax.xaxis.set_label_coords(1, 0.45)
    ax.set_ylabel(axis["y-name"] if "y-name" in axis else "y",
                  rotation='horizontal', fontsize=15)
    ax.yaxis.set_label_coords(0.5, 1.02)
    if("x-format" in axis):
        plt.gca().xaxis.set_major_formatter(
            mticker.FormatStrFormatter(axis["x-format"]))
    if("y-format" in axis):
        plt.gca().yaxis.set_major_formatter(
            mticker.FormatStrFormatter(axis["y-format"]))
    if("z-format" in axis and three_dimensional):
        plt.gca().zaxis.set_major_formatter(
            mticker.FormatStrFormatter(axis["z-format"]))

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
            x.append(graph["x_out"]["function"](i))
            y.append(graph["y_out"]["function"](i))

            z.append(graph["z_out"]["function"](
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
                       zorder=3, color=point["farbe"])
        else:
            ax.plot(x, y, color=point["farbe"], marker="o",
                    linewidth=linewidth * 2)

        if("annotation" in point and point["annotation"] == True):

            # Ergebnisse mit mehr als 3 Nachkommastellen werden zur Darstellung gerundet
            annotation = y if round(y, 3) == y else str(round(y, 3)) + "..."
            ax.annotate(f"({x}|{annotation})",
                        (x + 0.06, y - 0.5), fontsize=15)
        if("linien" in point and point["linien"] == True):

            plt.plot([0, x], [y, y],
                     linestyle="dotted", linewidth=2, color=point["farbe"])
            plt.plot([x, x], [0, y],
                     linestyle="dotted", linewidth=2, color=point["farbe"])
    plt.show()


golden_ratio = (1 + math.sqrt(5)) / 2


def binet(n):
    return complex((golden_ratio**n - (1 / -golden_ratio)**n) / math.sqrt(5))


# Reeler Teil mit gespiegeltem positivem Bereich
draw(graphs=[

],
    stepsize=0.01,
    axis={"x-name": "Re(z)", "y-name": "Im(z)", "y-format": '%.1f'},
    points=[
    {"x": x, "y": x, "z": 1, "farbe": "white",
     "linien": False, "annotation": False} for x in [-4, 4]
])
