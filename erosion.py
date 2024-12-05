import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

kernal = np.ones((5,5))
eroded = cv2.erode(binary, kernal, iterations = 1)

plt.figure(figsize=(12,8))

plt.subplot(122), plt.imshow(binary, cmap = 'gray'), plt.title('Orignal Img'), plt.axis('off')
plt.subplot(121), plt.imshow(eroded, cmap = 'gray'), plt.title('Eroded Img'), plt.axis('off')

plt.tight_layout()
plt.show()