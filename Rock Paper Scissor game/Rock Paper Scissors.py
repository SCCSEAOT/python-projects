import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

timer = 0
stateResult = False
startGame = False
detect = HandDetector(maxHands=1)
scores = [0, 0]
escape=True

while escape==True:
    imgBG = cv2.imread("resource/BG.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img, (0, 0), None, 0.646, 0.646)
    imgScaled = imgScaled[:, 35:375]

    #tofindhands
    hands, img = detect.findHands(imgScaled)
    if startGame:

        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer > 3:
                stateResult = True
                timer = 0
                if hands:
                    playerMove=None
                    hand = hands[0]
                    fingers = detect.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1
                    if fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2
                    if fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3
                    randomNumber = random.randint(1, 3)
                    imgAI = cv2.imread(f'resource/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBG=cvzone.overlayPNG(imgBG,imgAI, (217, 389))
                    # Player Wins
                    if (playerMove == 1 and randomNumber == 3) or \
                            (playerMove == 2 and randomNumber == 1) or \
                            (playerMove == 3 and randomNumber == 2):
                        scores[1] += 1

                    # AI Wins
                    if (playerMove == 3 and randomNumber == 1) or \
                            (playerMove == 1 and randomNumber == 2) or \
                            (playerMove == 2 and randomNumber == 3):
                        scores[0] += 1

    imgBG[292:602, 813:1153] = imgScaled


    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (217, 389))


    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    cv2.imshow("BG", imgBG)
    key=cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False
    if key == 27:
        escape= False
        cv2.destroyAllWindows()
