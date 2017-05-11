import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('lena.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 7, 0.05, 25)
corners = np.float32(corners)

for item in corners:
    x, y = item[0]
    cv2.circle(img, (x,y), 5, 255, -1)


plt.imshow(img)
plt.show()