import mediapipe as mp
import cv2
from pynput.mouse import Button, Controller
import time

# Initialize mediapipe and mouse controller
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mouse = Controller()

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize mediapipe hands and create a named window
hands = mp_hands.Hands()
#cv2.namedWindow("Hands", cv2.WINDOW_NORMAL)

while True:
    # Read a frame from the webcam
    ret, img = cap.read()
    if not ret:
        break

    # Flip the image horizontally for a mirrored view
    image = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)

    # Process the hand landmarks using mediapipe
    result = hands.process(image)

    # Convert the image back to BGR format for OpenCV
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks and connections on the image
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Extract hand landmark coordinates
            x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
            y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            x1 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
            y1 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y

            # Check if index finger is in a certain region
            if 0.25 < x < 0.75 and y < 0.5:
                x_normalized = (x - 0.25) / 0.5
                
                # Move the mouse cursor
                mouse.position = (int(1280 * x_normalized), int(800 * y))
                
                # Check for a mouse click gesture
                if abs((x - x1) * 100) <= 5 and abs((y - y1) * 100) <= 5:
                    print("Mouse click")
                    mouse.click(Button.left, 2)
                    time.sleep(2)
            
    # Resize and display the image
    #cv2.resizeWindow("Hands", 1280, 800)
    #cv2.imshow("Hands", image)
    
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()
