import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success,img = cap.read()

    if not success:
        break

    frameRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)

    if results.multi_hand_landmarks:
        for handType,handLms in zip(results.multi_handedness,results.multi_hand_landmarks):

            for id,lm in enumerate(handLms.landmark):
                h,w,c = img.shape 
                cx,cy,cz = int(lm.x*w),int(lm.y*h),int(lm.z*w)
                print(id,cx,cy,cz)
                cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
            if handType.classification[0].label == "Right":
                type='Left'
            else:
                type = 'Right'

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()