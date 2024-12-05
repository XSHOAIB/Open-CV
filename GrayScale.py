import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap='gray')

# plt.title('Gray Scale img')
# plt.axis('off')

plt.show()