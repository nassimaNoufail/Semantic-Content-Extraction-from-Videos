import numpy as np
import sys
import cv2

cap = cv2.VideoCapture('football.mp4')

while(True):

	ret, frame = cap.read()

	if ret==False: #To make sure no frame after video ends is read
		break

	cv2.imshow('frame', frame)

	if ret==False or cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
