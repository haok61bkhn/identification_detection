import sys
import argparse
from yolo.yolo import YOLO, detect_video
from PIL import Image
import cv2

class detect:
    def __init__(self):
        self.yolo=YOLO()
    def detect_img(self,path):
        if(True):
            image = None
            resimage=[]
            img = path
            try:
                image = Image.open(img)
                resimage=cv2.imread(img)
            except:
                print('Open Error! Try again!')
           
            r_image,resbox,labels= self.yolo.detect_image(image)
        return r_image,labels

# if __name__ == "__main__":
#     detector =detect()
#     image, labels = detector.detect_img("/home/hbhb/home_ubuntu/Intern/detection_licience_plate/keras-yolo3-master/1.jpg")
#     image.save("res.jpg")
#     print(labels)
