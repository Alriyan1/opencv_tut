import cv2
import numpy as np

image = cv2.imread('../Images/carImage.png')

imagehsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower = np.array([3,63,143])
upper = np.array([20,255,255])

mask = cv2.inRange(imagehsv,lower,upper)

imageResult = cv2.bitwise_and(image,image,mask=mask)

cv2.imshow('mask',mask)
cv2.imshow('output',imageResult)

cv2.waitKey(0)
cv2.destroyAllWindows()