import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

kernal  = np.ones((5,5), np.uint8)
dilate  = cv2.dilate(binary, kernal, iterations = 1)

plt.figure(figsize = (12,8))

plt.subplot(121), plt.imshow(binary, cmap = 'gray'), plt.title('Org'), plt.axis('off')
plt.subplot(122), plt.imshow(dilate, cmap = 'gray'), plt.title('next'), plt.axis('off')

plt.tight_layout()
plt.show()