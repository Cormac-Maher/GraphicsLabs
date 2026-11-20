import cv2
import numpy as np 
from matplotlib import pyplot as plt

imgOrig = cv2.imread('ATU.jpg',)

imgGray = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', imgGray)
cv2.waitKey(0)  
cv2.destroyAllWindows()
nrows = 3
ncols = 2

plt.subplot(nrows, ncols,1),plt.imshow(imgOrig, cmap = 'gray') 
plt.title('Original'), plt.xticks([]), plt.yticks([]) 
plt.subplot(nrows, ncols,2),plt.imshow(imgGray, cmap = 'gray') 
plt.title('GrayScale'), plt.xticks([]), plt.yticks([]) 


cv2.GaussianBlur()
KernelSizeWidth = 3
KernelSizeHeight = 3
imgOut1 = cv2.GaussianBlur(imgGray,(KernelSizeWidth, KernelSizeHeight),0)              # blue of 3x3
imgOut2 = cv2.GaussianBlur(imgGray,(KernelSizeWidth + 10, KernelSizeHeight + 10),0)    # blur of 13x13

plt.subplot(nrows, ncols,3),plt.imshow(imgOut1, cmap = 'gray') 
plt.title('3x3 Blur'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,4),plt.imshow(imgOut2, cmap = 'gray') 
plt.title('13x13 Blur'), plt.xticks([]), plt.yticks([])

sobelHorizontal = cv2.Sobel(imgGray,cv2.CV_64F,1,0,ksize=5)  # x dir 
sobelVertical   = cv2.Sobel(imgGray,cv2.CV_64F,0,1,ksize=5)  # y dir

plt.subplot(nrows, ncols,5),plt.imshow(sobelHorizontal, cmap = 'gray')   # plotting images
plt.title('3x3 Blur'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,6),plt.imshow(sobelVertical, cmap = 'gray') 
plt.title('13x13 Blur'), plt.xticks([]), plt.yticks([])
plt.show()
sobelVertical   = cv2.Sobel(sobelHorizontal,cv2.CV_64F,0,1,ksize=5)  # combined image