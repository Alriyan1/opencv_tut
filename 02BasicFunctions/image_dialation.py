import cv2
import numpy as np

image = cv2.imread('../Images/5606295.jpg')
image=cv2.resize(image,(800,400))

image_canny = cv2.Canny(image,100,100)

kernel = np.ones((3,3),np.uint8)

image_dialation = cv2.dilate(image_canny,kernel,iterations=1)

cv2.imshow('imagecanny',image_canny)
cv2.imshow('image_dialation',image_dialation)

cv2.waitKey(0)
cv2.destroyAllWindows()