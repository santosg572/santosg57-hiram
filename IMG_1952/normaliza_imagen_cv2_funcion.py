# https://www.geeksforgeeks.org/computer-vision/normalize-an-image-in-opencv-python/

import cv2

# Read grayscale image

def NormalizaIMG(file=''):
   image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

   # Normalize image
   normalized_image = cv2.normalize(
     image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
#   return (image, normalized_image)
   return (image, normalized_image) 

pat = 'temporal/'

num1 = 397

file1 = 'fotograma_0O_'+ str(num1)

images1 = NormalizaIMG(pat+file1+'.png')

cv2.imwrite(file1+'_N'+'.png', images1[1])


