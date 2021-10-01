import cv2
import numpy as np
import socket
import ctypes
import struct
from datetime import datetime

today = datetime.now()

cap =[]
cap.append(cv2.VideoCapture(0))
cap.append(cv2.VideoCapture(2))

cap[0].set(cv2.CAP_PROP_FPS, 15)
cap[1].set(cv2.CAP_PROP_FPS, 15)

cap[0].set(3, 1280)
cap[0].set(4, 720)

cap[1].set(3, 1280)
cap[1].set(4, 720)


img_counter=0

def grab(num):
    res, im = cap[num].read()
    return(res,im)

def grabSBS():
    res, imLeft = grab(1)
    res, imRight = grab(0)
    imSBS=np.concatenate((imLeft, imRight), axis=1)
    return res,imSBS

while(True):
    res, imLeft = grab(0)
    res, imRight = grab(1)
    imSBS=np.concatenate((imLeft, imRight), axis=1)
    cv2.imshow("win", imSBS)
    k = cv2.waitKey(1)
    
    if k%256 == 27:
        #ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        #SPACE pressed
        img_name = "picture-time-{}.png".format(today)
        cv2.imwrite(img_name, imSBS)
        print("{} written!".format(img_name))
        img_counter += 1

cap[0].release()
cap[1].release()

cv2.destroyAllWindows()
    
    