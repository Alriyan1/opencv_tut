import cv2
import numpy as np

image = cv2.imread('../Images/card1.jpg')

w,h = 250,350

pts1 = np.float32([[112,223],[280,192],[158,475],[348,435]])

pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

image_output = cv2.warpPerspective(image,matrix,(w,h))

cv2.imshow('image',image)
cv2.imshow('image_output',image_output)

cv2.waitKey(0)
cv2.destroyAllWindows()
