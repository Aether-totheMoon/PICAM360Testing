import cv2
import numpy as np
from datetime import datetime

today = datetime.now()

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(2)
cam1.set(3, 1280)
cam1.set(4, 720)
cam2.set(3, 1280)
cam2.set(4, 720)

ret, frame1 = cam1.read()
ret, frame2 = cam2.read()
row, cols, ret1 = frame1.shape
row, cols, ret = frame2.shape


cv2.namedWindow("test")

img_counter=0

while True:
    ret1, frame1 = cam1.read()
    ret, frame2 = cam2.read()
    if not ret1:
        print("Failed to grab frame")
        break
    cv2.imshow("test", frame1)

    k = cv2.waitKey(1)
    if k%256 == 27:
        #ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        #SPACE pressed
        img_name1 = "1picture-time-{}.png".format(today)
        img_name2 = "2picture-time-{}.png".format(today)
        cv2.imwrite(img_name1, frame1)
        cv2.imwrite(img_name2, frame2)

        print("{} written!".format(img_name))
        img_counter += 1

cam1.release()
cam2.release()

cv2.destroyAllWindows()

