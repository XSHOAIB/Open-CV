import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg', cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure(figsize= (12,8))

plt.subplot(121), plt.imshow(gray, cmap = 'gray'), plt.title('BGR'), plt.axis('off')
plt.subplot(122), plt.imshow(img2, cmap = 'gray'), plt.title('GRAY'), plt.axis('off')

plt.tight_layout()
plt.show()