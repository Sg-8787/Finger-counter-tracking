import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
 
      # Hand tracking
       detector = HandDetector(detectionCon=0.8, maxHands=2) # probability of detection, max hands to detect 
       while True:
       success, img = cap.read()

        hands, img = detector.findHands(img)

        if hands:

        hand = hands[0]
        lmList = hand["lmList"]
        hand["type"]  # "Right" ya "Left"
        fingers = []
        for hand in hands:
         print(hand["type"])

        # Thumb
        if lmList[4][0] > lmList[3][0]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Fingers
        for id in range(1, 5):
            if lmList[id * 4 + 1][1] < lmList[id * 4 - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

         print(fingers.count(1))
         cv2.imshow("Finger Count", img)
          
        if cv2.waitKey(1) == 27: #Ascii code for ESC key,to exit the loop
        break
