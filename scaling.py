import matplotlib.pyplot as plt
import numpy as np

points = np.array([
    [1, 0], 
    [4, 0], 
    [4, 4], 
    [1, 0]
])

sx = 2
sy = 2

scaled = points * [sx, sy]

plt.plot(points[:, 0], points[:, 1], 'b-', label='original')
plt.plot(scaled[:, 0], scaled[:, 1], 'r-', label='scaled')

plt.show()