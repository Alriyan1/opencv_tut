import cv2

image = cv2.imread('../Images/128706.png')

image=cv2.resize(image,(800,400))

image_canny = cv2.Canny(image,100,100)
image_canny2 = cv2.Canny(image,150,200)

cv2.imshow('image',image)
cv2.imshow('image_canny',image_canny)
cv2.imshow('image_canny2',image_canny2)

cv2.waitKey(0)
cv2.destroyAllWindows()