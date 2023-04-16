#INITIAL SETUP
#----------------------------------------------------------------
import os
import time

import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
folderPath = 'frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]
intro = graphic[0];
kill =graphic[1];
winner = graphic[2];
camShow = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)

camH, camW = camShow.shape[0], camShow.shape[1]
showFrame[0:camH, -camW:] = camShow

cv2.imshow('Squid Game', showFrame)
if cv2.waitKey(10) & 0xFF == ord('q'):
     break

detector = HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77)
#sets the minimum confidence threshold for the detection
TIMER_MAX = 45
TIMER = TIMER_MAX
maxMove = 6500000
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)


#INITILIZING GAME COMPONENTS
#----------------------------------------------------------------
folderPath1 = 'img'
mylist1 = os.listdir(folderPath1)
graphic1 = [cv2.imread(f'{folderPath1}/{imPath}') for imPath in mylist1]
sqr_img = graphic1[1];
mlsa =  graphic1[0];
#INTRO SCREEN WILL STAY UNTIL Q IS PRESSED

while True:
    cv2.imshow('Cookiecutter', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

gameOver = False
NotWon =True
#GAME LOGIC UPTO THE TEAMS
#-----------------------------------------------------------------------------------------
while not gameOver:
        continue
#LOSS SCREEN
if NotWon:
    for i in range(10):
       #show the loss screen from the kill image read before
    while True:
        #show the loss screen from the kill image read before and end it after we press q

else:
#WIN SCREEN
#show the win screen from the winner image read before and end it after we press q
         cv2.imshow('Cookiecutter', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
        # cv2.imshow('shit',cv2.resize(graphic[3], (0, 0), fx = 0.5, fy = 0.5))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()
