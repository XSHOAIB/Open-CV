import cv2
import matplotlib.pyplot as plt

img = cv2.imread('2.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('IMAGE', img)
k = cv2.waitKey(0)
if k == 27: # ESC key
  cv2.destroyAllWindows()
elif k == ord('s'): # 's' key to save
  cv2.imwrite("C:/Users/miray/OneDrive/Pictures/saved_image.jpg",
img)
  cv2.destroyAllWindows()