import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg')

blur = cv2.blur(img, (5,5))
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

plt.figure(figsize=(15,5))

plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('ORG'), plt.axis('off')
plt.subplot(132), plt.imshow(cv2.cvtColor(blur,cv2.COLOR_BGR2RGB)), plt.title('Blur'), plt.axis('off')
plt.subplot(133), plt.imshow(cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB)), plt.title('Bilateral'), plt.axis('off')

plt.tight_layout()
plt.show()