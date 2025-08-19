import cv2
import numpy as np

image = cv2.imread('../Images/image2.jpg')

print(image.shape)

imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
imageGray = cv2.cvtColor(imageGray,cv2.COLOR_GRAY2BGR)

print(imageGray.shape)

imagHor = np.hstack((image,image,image))
imagVer = np.vstack((image,image,imageGray))

cv2.imshow('image horizontal',imagHor)
cv2.imshow('image vertical',imagVer)

cv2.waitKey(0)
cv2.destroyAllWindows()
