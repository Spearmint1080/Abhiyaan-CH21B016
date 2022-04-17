# importing libraries
import cv2
import numpy as np

#Opening file
cam = cv2.VideoCapture('virat_test_pothole.mp4')


if (cam.isOpened()== False):
    print("Error opening video file")


while(cam.isOpened()):
	
    # Gets each Frame
    ret, frame = cam.read()
    if ret == True:

       #Draws White border at specified location
        frame =  cv2.rectangle(frame, (100,100), (200, 200), (255,255,255), 2)
        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break


    cam.release()

    cv2.destroyAllWindows()
