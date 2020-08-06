
import cv2
import os

def data(n):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height
 
    face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    face_id = 1
    print("\n  Initializing face capture. Look the camera and wait ...")

    count = 0
 
    while (n>0):
        ret, img = cam.read()
        frame = cv2.flip(frame, -1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        cv2.putText(img, "scanning, press ESC to stop", (100,100), font, 1, (0,255,255), 2)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
 
        # Save the captured image into the datasets folder
            cv2.imwrite("./dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 100: # Take 30 face sample and stop video
            break
# Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows() 

