import cv2
import numpy as np
from datetime import datetime

today = datetime.now()

cam = cv2.VideoCapture(0)
cam.set(3, 1080)
cam.set(4, 720)

ret, frame = cam.read()
row, cols, ret = frame.shape

cv2.namedWindow("test")

img_counter=0

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        #ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        #SPACE pressed
        img_name = "picture-time-{}.png".format(today)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
