import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

print(dir(cv2))

lista_cv2 = ['absdiff', 'threshold', 'findContours', 'boundingRect', 'imread']

for ss in lista_cv2:
   print('** &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& **')
   print(help(eval('cv2.'+ss)))



