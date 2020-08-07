import cv2
import numpy as np
from PIL import Image
import os
import facedataset

# Path for face image database
path = 'dataset'
#recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
 
# function to get the images and label data
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')
        id = 1
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids
 

def train(n):
    if n>0:
        facedataset.data(1)
        faces,ids = getImagesAndLabels(path)
        detector.train(faces, np.array(ids))
        detector.save('training/trainer.yml')
        print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
    else:
        pass
