import mediapipe as mp
import cv2
from pynput.mouse import Button, Controller

mp_drawing= mp.solutions.drawing_utils
mp_drawing_styles= mp.solutions.drawing_styles
mp_hands=mp.solutions.hands
mouse=Controller()


cap=cv2.VideoCapture(0)
hands=mp_hands.Hands()
cv2.namedWindow("Hands", cv2.WINDOW_NORMAL)
c=0

while True:
    data, img= cap.read()
    image=cv2.cvtColor(cv2.flip(img,1),cv2.COLOR_BGR2RGB)
    result=hands.process(image)
    
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS)
            x=(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x)
            y=(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y)
            x1=(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x)
            y1=(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y) 
            if x*100>25 and x*100<75 and y*100<50:
                x=(x-0.25)/(0.50)
                print(x) 
                wristx=(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x)
                wristy=(hand_landmarks.landmap--
                
                rk[mp_hands.HandLandmark.WRIST].y)
                mouse.position = (int(1280*x),int(800*y))
                if abs((x-x1)*100)<=5 and abs((y-y1)*100)<=5 and abs((wristy-y1)*100)>50:
                    print(c,"mouse click")
                    #mouse.click(Button.left,1)
                #print(abs((x-x1)*100), abs((y-y1)*100))

    cv2.resizeWindow("Hands", 1280, 800)        
    cv2.imshow("Hands", image)
    cv2.waitKey(1)
