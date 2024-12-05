import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

#Adaptive thresholding 
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

plt.figure(figsize = (10 ,8))
plt.subplot(121), plt.imshow(th1, cmap = 'gray'), plt.title('Adaptive Mean Thresholding'), plt.axis('off')

plt.subplot(122), plt.imshow(th2, cmap = 'gray'), plt.title('Adaptive Gaussian Thresholding'),

plt.show()
