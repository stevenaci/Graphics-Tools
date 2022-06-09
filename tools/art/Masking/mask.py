import cv2 as cv
import numpy as np


class Mask:
	data:np.array = 0
	res:np.array = 0

	def __init__(self, img, hsv_range):
		self.create_mask(img, hsv_range)

	def create_mask(self, img, r):
		hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
		self.data = cv.inRange(hsv, r.low, r.hi)
		self.res = cv.bitwise_and(img,img, mask=self.data)
