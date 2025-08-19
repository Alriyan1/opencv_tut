import cv2

image = cv2.imread('../Images/1070182.jpg')

image=cv2.resize(image,(800,400))

image_blur = cv2.GaussianBlur(image,(7,7),0)

cv2.imshow('image',image)
cv2.imshow('image_blur',image_blur)

cv2.waitKey(0)

cv2.destroyAllWindows()