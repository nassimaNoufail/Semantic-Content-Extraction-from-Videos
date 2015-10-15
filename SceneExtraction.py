import numpy as np
import sys
import cv2

cap = cv2.VideoCapture('football.mp4')
counter=0
while(True):

	ret, frame = cap.read()

	if ret==False: #To make sure no frame after video ends is read
		break
	
	cv2.imshow('frame', frame)
	cv2.imwrite("./Frames/Scene_"+`counter`+".jpg",frame)
	counter=counter+1
	if ret==False or cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
