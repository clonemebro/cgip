import matplotlib.pyplot as plt
import numpy as np

points = np.array([
    [1, 0], 
    [3, 0], 
    [3, 3],
    [1, 0]
])

angle = np.radians(90)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)]
])

rotated = points @ rotation.T

plt.plot(points[:, 0], points[:, 1], 'b-', label = 'original')
plt.plot(rotated[:, 0], rotated[:, 1], 'r-', label = 'rotated')

plt.axis("equal")
plt.show()