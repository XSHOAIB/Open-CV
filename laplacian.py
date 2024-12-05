import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(img, cv2.CV_64F)

plt.imshow(laplacian, cmap = 'gray'), plt.title('bhiaii'), plt.axis('off')

plt.show()