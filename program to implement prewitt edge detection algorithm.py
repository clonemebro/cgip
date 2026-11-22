import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("image.jpg", 0)

kernal_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1] 
])

kernal_y = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

prewitt_x = cv2.filter2D(img, -1, kernal_x)
prewitt_y = cv2.filter2D(img, -1, kernal_y)

prewitt = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')

plt.subplot(1, 2, 2)
plt.imshow(prewitt, cmap='gray')

plt.show()