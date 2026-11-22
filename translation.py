import matplotlib.pyplot as plt
import numpy as np

points = np.array([
    [1, 1],
    [4, 2],
    [2, 3],
    [1, 1]
])

tx = 2
ty = 3

translated = points + [tx, ty]

plt.plot(points[:, 0], points[:, 1], 'b-', label = 'original')
plt.plot(translated[:, 0], translated[:, 1], 'r-', label = 'translated')

plt.xlabel("x-label")
plt.ylabel("y-label")
plt.grid(True)
plt.title("Translation")
plt.axis("equal")
plt.show()