import cv2
import mediapipe as mp
import time
import HandTrackerModule as htm


pTime, cTime = 0, 0
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)     # id of web cam
video.set(3,640)                # width
video.set(4,480)                # height
tracker = htm.HandTracker()
while True:
    success, img = video.read()
    img = tracker.findHands(img, draw=True )
    lmList = tracker.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3) # to show FPS

    cv2.imshow("video", img)
    if  cv2.waitKey(1) & 0xFF ==ord('q'):       # enter q to stop video
        break