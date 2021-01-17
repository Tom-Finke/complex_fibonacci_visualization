This project visualizes complex fibonacci numbers both in 3d and 2d graphs.
Images can be saved by clicking the "save" icon in the pyplot gui created by the python script.

A Graph can be created by calling the draw function of fibo_visualization.py
It takes the following parameters:

- graphs : A list of dictionaries, describing all graphs do be drawen

  - interval: list of length 2, start and end point of the graph (e.g. [0.0, 7.3])
  - x_out, y_out (z_out): a function (e.g. lambda function) for calculating the value on each axis. If z_out is set for at least one graph, the resulting visualization will be in 3d

  - color: a pyplot color as defined in https://matplotlib.org/tutorials/colors/colors.html

- stepsize: float, how detailed the graph should be drawn (e.g 0.1 --> rough, 0.0001 --> very fine)

- axes: description each the axis.

  - name: label of the axis
  - (format): optional format, e.g "%i" for adding an i to a imaginary number axis

- points: a list of points to be drawn. For each point:
  - x: x-position
  - y: y-position
  - (z): z-position
  - color: pyplot color
  - lines: bool, wether or not to draw lines from the point to the axes
  - annotation: bool, wether or not annotate the point with its coordinates
