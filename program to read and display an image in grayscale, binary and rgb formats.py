import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(1, 3, 1)
plt.imshow(gray, cmap = 'gray')

plt.subplot(1, 3, 2)
plt.imshow(binary, cmap = 'gray')

plt.subplot(1, 3, 3)
plt.imshow(rgb)

plt.show()