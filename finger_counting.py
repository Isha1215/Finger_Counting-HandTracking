import numpy
import cv2
import os
import time
import HandTrackingmodule as htm

cap=cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,640)
path="resources"
list=os.listdir(path)
images=[]
ptime=0
for i in list:
    im=cv2.imread(path+"/"+i)
    images.append(im)
tips=[4,8,12,16,20]
while True:
    success,img=cap.read()
    detector=htm.HandDetector()
    detector.Hands_draw(img)
    landmarks,box=detector.FindPosition(img,draw=False)
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, f'FPS: {int(fps)}', (500, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
    if(len(landmarks)!=0):
        fingers = []
        if landmarks[tips[0]][1]<landmarks[tips[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for i in range(1,5):
            if landmarks[tips[i]][2]<landmarks[tips[i]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        num=fingers.count(1)
        h,w,c=images[num-1].shape
        img[0:h,0:w]=images[num-1]
        cv2.rectangle(img,(0,300),(170,450),(255,0,0),cv2.FILLED)
        cv2.putText(img,str(num),(80,370),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,0),2)

    cv2.imshow("image",img)
    if cv2.waitKey(1) and 0XFF==ord('p'):
        break