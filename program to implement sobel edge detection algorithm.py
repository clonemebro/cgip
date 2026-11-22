import matplotlib.pyplot as plt
import cv2

img = cv2.imread("image.jpg", 0)

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
soble_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

sobel = cv2.magnitude(sobel_x, soble_y)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')

plt.subplot(1, 2, 2)
plt.imshow(sobel, cmap='gray')

plt.show()