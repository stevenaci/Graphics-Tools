import cv2 as cv
import numpy as np

from tools.art.colors.colors import HSVColorange


class Mask:
	data:np.array = 0
	res:np.array = 0

	def __init__(self, img, hsv_range: HSVColorange):
		self.create_mask(img, hsv_range)

	def create_mask(self, hsv_img, r: HSVColorange):
		# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

		self.res = cv.bitwise_and(
			hsv_img.obj, hsv_img.obj, 
			mask=cv.inRange(hsv_img.obj, r.low, r.hi)
		)
		self.res = cv.cvtColor(self.res, cv.COLOR_HSV2BGR)
		self.res = self.replace_color_with_transparency(self.res)

	def replace_color_with_transparency(self, img, color = [0,0,0]):

		mask = np.where((img==color).all(axis=2), 0, 255).astype(np.uint8)
		img = cv.cvtColor(img, cv.COLOR_BGR2BGRA)
		img[:, :, 3] = mask
		return img
		