import matplotlib.pyplot as plt
import cv2

img = cv2.imread("image.jpg", 0)

equalized = cv2.equalizeHist(img)

plt.subplot(2, 2, 1)
plt.imshow(img, cmap = 'gray')

plt.subplot(2, 2, 2)
plt.imshow(equalized, cmap='gray')

plt.subplot(2, 2, 3)
plt.hist(img.ravel(), 256, [0, 256])

plt.subplot(2, 2, 4)
plt.hist(equalized.ravel(), 256, [0, 256])

plt.show()