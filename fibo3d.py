'''
======================
Triangular 3D surfaces
======================

Plot a 3D surface with a triangular mesh.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math


# n_radii = 8
# n_angles = 36

# # Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
# radii = np.linspace(0.125, 1.0, n_radii)
# angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)

# # Repeat all angles for each radius.
# angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

# # Convert polar (radii, angles) coords to cartesian (x, y) coords.
# # (0, 0) is manually added at this stage,  so there will be no duplicate
# # points in the (x, y) plane.
# x = np.append(0, (radii*np.cos(angles)).flatten())
# y = np.append(0, (radii*np.sin(angles)).flatten())

# # Compute z to make the pringle surface.
# z = np.sin(-x*y)


# Make data.
golden_ratio = (1 + math.sqrt(5)) / 2


def fib(n):
    return complex((golden_ratio**n - (1 / -golden_ratio)**n) / math.sqrt(5))


cnums = []
x = []
for i in np.arange(-10, 10.0, 0.001):
    i = float(i)
    print(i)
    cnums.append(fib(i))
    x.append(i)

# cnums = np.arange(5) + 1j * np.arange(6,11)
y = [x.real for x in cnums]
z = [x.imag for x in cnums]

fig = plt.figure()
ax = fig.gca(projection='3d')


ax.set_xlabel('realer input')
ax.set_ylabel('realer output')
ax.set_zlabel('imaginärer output')


linewidth = 20
ax.scatter(x, y, z, s=linewidth, zorder=1)
ax.scatter([2], [1], [0], zorder=2, s=linewidth)
ax.scatter([3], [2], [0], zorder=2, s=linewidth)
ax.scatter([4], [3], [0], zorder=2, s=linewidth)
ax.scatter([5], [5], [0], zorder=2, s=linewidth)
ax.scatter([6], [8], [0], zorder=2, s=linewidth)
ax.scatter([7], [13], [0], zorder=2, s=linewidth)
plt.show()
