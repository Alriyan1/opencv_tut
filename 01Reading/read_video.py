import cv2

cap = cv2.VideoCapture('../Videos/video1.mp4')

while True:
    success, img = cap.read()
    if success:
        cv2.imshow('video',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()