# https://www.geeksforgeeks.org/python/histograms-equalization-opencv/

import cv2
import numpy as np
import matplotlib.pyplot as plt

pat = 'temporal/'
file = 'fotograma_0O_393.png'

img = cv2.imread(pat+file, 0)  
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))

plt.figure(figsize=(10, 5))
plt.imshow(res, cmap='gray')  
plt.title("Original vs Equalized Image")
plt.axis('off')  
plt.show()


