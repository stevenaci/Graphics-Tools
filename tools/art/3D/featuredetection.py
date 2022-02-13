import numpy as np
import cv2 as cv
from datetime import datetime

def timed_(f):
    def wrapper(*args):
        e1 = cv.getTickCount()
        res = f(*args)
        e2 = cv.getTickCount()
        t = (e2 - 
            e1
        ) / cv.getTickFrequency()
        print("\n{} elapsed in {} seconds.".format(f, t))
        return res
    return wrapper



class FeatureField():

    def __init__(self) -> None:
        pass

    @timed_
    def sift_keypoints(self, fname) -> cv.KeyPoint:
        img = cv.imread(fname)

        gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        sift = cv.SIFT_create(1231)
        
        kp, des = sift.detectAndCompute(gray,None)
        img = cv.drawKeypoints(gray, kp, img)
        cv.imwrite(
            str(datetime.now().timestamp())+'.jpg',
            img)
        return kp

class DepthField:

    @staticmethod
    def generate(fname):
        pass

#features = FeatureField()
#keypoints = features.sift_keypoints('m.jpg')