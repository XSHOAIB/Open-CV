import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg')

B, G, R = cv2.split(img)

plt.subplot(131), plt.imshow(B, cmap='Blues'), plt.title('Blue'), plt.axis('off')
plt.subplot(132), plt.imshow(G, cmap='Greens'), plt.title('Greens'), plt.axis('off')
plt.subplot(133), plt.imshow(R, cmap='Reds'), plt.title('Reds'), plt.axis('off')

plt.show()