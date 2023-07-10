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


while True:
    data, img= cap.read()
    image=cv2.cvtColor(cv2.flip(img,1),cv2.COLOR_BGR2RGB)
    result=hands.process(image)
    
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS)
            x=(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x)*100
            y=(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y)*100            
            cv2.putText(image,"O",(int(1280/-x),int(800/-y)),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255),1,cv2.LINE_AA, False)
            mouse.position = (x,y)
            
    cv2.resizeWindow("Hands", 1280, 800)        
    cv2.imshow("Hands", image)
    cv2.waitKey(1)
