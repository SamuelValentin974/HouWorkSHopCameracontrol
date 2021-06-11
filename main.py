##
## EPITECH PROJECT, 2021
## Emilie.baunifais_Wkshop
## File description:
## wk
##

import cv2
import mediapipe as mp

def draw_plan():
    cam = cv2.VideoCapture(0)
    mpHand = mp.solutions.hands
    hands = mpHand.Hands()
    mpDraw = mp.solutions.drawing_utils
    while True:
        ret, frame = cam.read()
        if not ret:
            printf("unable to open camera")
            break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handlms, mpHand.HAND_CONNECTIONS)
            cv2.imshow("Camera", frame)
        # for id, lm in enumerate(handlms.landmark):
        #    h, w, c = frame.shape
        #    [...], [...] = int([...]), int([...])
            if cv2.waitKey(1) == ord('q'):
                break
    cv2.destroyAllWindows()
draw_plan()