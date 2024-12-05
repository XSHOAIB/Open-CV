import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)

thresh1, binary = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
thresh2, binary_inv = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
thresh3, trunc = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
thresh4, tozero = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
thresh5, tozero_inv = cv2.threshold(img,120,255, cv2.THRESH_TOZERO_INV)

plt.figure(figsize= (12, 8))

plt.subplot(231), plt.imshow(img, cmap='gray'), plt.title('Orignal Image'), plt.axis('off')
plt.subplot(232), plt.imshow(binary, cmap = 'gray'), plt.title('Binary Image'), plt.axis('off')
plt.subplot(233), plt.imshow(binary_inv, cmap = 'gray'), plt.title('Binary Inv'), plt.axis('off')
plt.subplot(234), plt.imshow(trunc, cmap = 'gray'), plt.title('Trunc Img'), plt.axis('off')
plt.subplot(235), plt.imshow(tozero, cmap = 'gray'), plt.title('Tozero Img'), plt.axis('off')
plt.subplot(236), plt.imshow(tozero_inv, cmap = 'gray'), plt.title('Tozero Inv'), plt.axis('off')

plt.tight_layout()
plt.show()