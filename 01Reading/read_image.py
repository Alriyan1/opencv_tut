import cv2

image = cv2.imread('../Images/5606295.jpg')

cv2.imshow('image',image)

cv2.waitKey(1000)

cv2.destroyAllWindows()
