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
    # Beschriftung der Achsen einfügen und deren Position anpassen
    ax.set_xlabel(
        axes["x"]["name"] if "x" in axes and "name" in axes["x"] else "x", fontsize=15)
    ax.xaxis.set_label_coords(1, 0.45)
    ax.set_ylabel(axes["y"]["name"] if "y" in axes and "name" in axes["y"] else "y",
                  rotation='horizontal', fontsize=15)
    ax.yaxis.set_label_coords(0.5, 1.02)

    # Eruieren ob der Graph 3d oder 2d wird. 3D wenn mind. 1 Graph ein z_out parameter besitzt
    three_dimensional = True if True in [
        True for graph in graphs if "z_out" in graph] else False

    if(three_dimensional):
        ax = fig.gca(projection='3d')
        ax.set_zlabel(axes[z]["name"]
                      if "z" in axes and "name" in axes["z"] else "z")

    # Skala Beschriftungen formatieren
    if("x" in axes and "format" in axes["x"]):
        plt.gca().xaxis.set_major_formatter(
            mticker.FormatStrFormatter(axes["x"]["format"]))
    if("y" in axes and "format" in axes["y"]):
        plt.gca().yaxis.set_major_formatter(
            mticker.FormatStrFormatter(axes["y"]["format"]))
    if("z" in axes and "format" in axes["z"] and three_dimensional):
        plt.gca().zaxis.set_major_formatter(
            mticker.FormatStrFormatter(axes["z"]["format"]))
    # Größer der Skala Striche anpassen
    ax.tick_params(axis='x', labelsize=15, pad=10)
    ax.tick_params(axis='y', labelsize=15, pad=20)
    ax.tick_params(axis='z', labelsize=15, pad=20) if three_dimensional else 0

    # Wenn 2D Graph, Koordinatenachsen anpassen (Zu Ursprung verschieben) und Pfeile an Koordinatenachsen zeichnen
    if(not three_dimensional):
        # Koordinatensystem anpassen --> 2 Achsen die sich in Ursprung treffen
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_linewidth(2)
        ax.spines['bottom'].set_linewidth(2)
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
                transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot((0), (1), ls="", marker="^", ms=10, color="k",
                transform=ax.get_xaxis_transform(), clip_on=False)

    # Jeden Graph zeichnen
    for graph in graphs:
        x, y, z = [], [], []
        for i in [x * stepsize for x in range(
                int(graph["interval"][0] * (1 / stepsize)),
                int(graph["interval"][1] * (1 / stepsize)))]:
            x.append(graph["x_out"](i))
            y.append(graph["y_out"](i))

        # Wenn 3D: z-Achse befüllen und Scatterplot zeichnen
        if(three_dimensional):
            z.append(graph["z_out"](
                i) if "z_out" in graph else 0)  # Wenn der Graph keine z-Achse besitzt wird jeder z-wert mit 0 befüllt
            ax.scatter(x, y, z, s=linewidth, zorder=1, color=graph["color"])
        else:
            ax.plot(x, y, linewidth=linewidth, color=graph["color"])

    # Jeden Punkt zeichnen
    for point in points:
        # Float werte, die auf 10 Nachkommastellen ihren ganzzahlig gerundeten Werten entsprechen werden gerundet, da von einer Abweichung bei der Computer bedingten ungenauigkeit ausgegangen wird
        for i in ["x", "y", "z"]:
            point[i] = (int(point[i]) if round(point[i], 10) == int(
                point[i]) else point[i]) if i in point else 0

        if(three_dimensional):
            ax.scatter(point["x"], point["y"], point["z"], s=linewidth * 2,
                       zorder=3, color=point["color"] if "color" in point else "C0")
        else:
            ax.plot(point["x"], point["y"], color=point["color"] if "color" in point else "C0", marker="o",
                    linewidth=linewidth * 2)

        if("annotation" in point and point["annotation"] == True):
            # Ergebnisse mit mehr als 3 Nachkommastellen werden zur Darstellung gerundet und als z.B. "3.141..."" angegeben
            x_annotation = point["x"] if round(
                point["x"], 3) == point["x"] else str(round(point["x"], 3)) + "..."
            y_annotation = point["y"] if round(
                point["y"], 3) == point["y"] else str(round(point["y"], 3)) + "..."

            ax.annotate(f"({x_annotation}|{y_annotation})",
                        (point["x"], point["y"]), fontsize=15)

        if("lines" in point and point["lines"] == True and not three_dimensional):
            plt.plot([0, point["x"]], [point["x"], point["y"]],
                     linestyle="dotted", linewidth=2, color=point["color"] if "color" in point else "C0")
            plt.plot([point["x"], point["x"]], [0, point["y"]],
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
     "lines": False, "annotation": True} for x in range(0, 6)
])
