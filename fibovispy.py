""" scatter using MarkersVisual """

import numpy as np
import sys

from vispy import app, visuals, scene
import math


# build your visuals, that's all
Scatter3D = scene.visuals.create_visual_node(visuals.MarkersVisual)

# The real-things : plot using scene
# build canvas
canvas = scene.SceneCanvas(keys='interactive', show=True, bgcolor='w')

# Add a ViewBox to let the user zoom/rotate
view = canvas.central_widget.add_view()
view.camera = 'turntable'
view.camera.fov = 45
view.camera.distance = 500

golden_ratio = (1 + math.sqrt(5)) / 2


def fib(n):
    return complex((golden_ratio**n - (1 / -golden_ratio)**n) / math.sqrt(5))


r = [0, 10]
scale = 10
pos = np.zeros((r[1] * scale, 3))
colors = np.ones((r[1] * scale, 4), dtype=np.float32)
for i in range(r[0] * scale, r[1] * scale):

    fibo = fib(i / scale)
    pos[i] = i / scale, fibo.real, fibo.imag
    colors[i] = (i / (r[1] * scale), 1.0 - i / (r[1] * scale), 0, 0.8)


# plot ! note the parent parameter
p1 = Scatter3D(parent=view.scene)
p1.set_gl_state('translucent', blend=True, depth_test=True)
p1.set_data(pos, face_color=colors, symbol='o', size=2,
            edge_width=0.5)


xax = scene.Axis(pos=[[0, 0, 0], [1, 0, 0]], tick_direction=(
    0, -1, 0), axis_color='r', tick_color='r', text_color='r', font_size=16, parent=view.scene)

yax = scene.Axis(pos=[[0, 0], [0, 1]], tick_direction=(-1, 0), axis_color='g',
                 tick_color='g', text_color='g', font_size=16, axis_width=200, parent=view.scene)

zax = scene.Axis(pos=[[0, 0], [-1, 0]], tick_direction=(0, -1), axis_color='b',
                 tick_color='b', text_color='b', font_size=16, parent=view.scene)

# run
if __name__ == '__main__':
    if sys.flags.interactive != 1:
        app.run()
