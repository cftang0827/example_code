# Python opencv sample code for Averaging blur
# http://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('lena.jpg')
kernel = np.ones((13,13),np.float32)/169
dst = cv2.filter2D(img,-1,kernel) 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()