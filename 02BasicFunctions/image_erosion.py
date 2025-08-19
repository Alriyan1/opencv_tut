import cv2
import numpy as np

image = cv2.imread('../Images/1070182.jpg')

image = cv2.resize(image,(800,400))

image_canny = cv2.Canny(image,100,100)

kernal = np.ones((3,3),np.uint8)
image_dialation = cv2.dilate(image_canny,kernal,iterations=1)
image_erosion = cv2.erode(image_dialation,kernal,iterations=1)

cv2.imshow('image_dialation',image_dialation)
cv2.imshow('image_erosion',image_erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()