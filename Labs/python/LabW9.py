import cv2
import numpy as np 
from matplotlib import pyplot as plt

imgOrig = cv2.imread('ATU.jpg',)

imgGray = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', imgGray)
cv2.waitKey(0)  
cv2.destroyAllWindows()
nrows = 2
ncols = 1

plt.subplot(nrows, ncols,1),plt.imshow(imgOrig, cmap = 'gray') 
plt.title('Original'), plt.xticks([]), plt.yticks([]) 
plt.subplot(nrows, ncols,2),plt.imshow(imgGray, cmap = 'gray') 
plt.title('GrayScale'), plt.xticks([]), plt.yticks([]) 
plt.show()

