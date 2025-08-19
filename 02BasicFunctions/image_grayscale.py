import cv2

image = cv2.imread('../Images/1070182.jpg')
image=cv2.resize(image,(800,600))

img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('image',image)
cv2.imshow('image_gray',img_gray)

cv2.waitKey(0)

cv2.destroyAllWindows()