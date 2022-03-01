from ast import Raise
import cv2 as cv
import numpy as np
from tools.art.cv_img import HSVImg, CVImg
from tools.art.hsvcolors import HSVColor, HSVColorange

class Mask:
	data:np.array = 0
	res:np.array = 0

	def __init__(self, img, hsv_range):
		self.create_mask(img, hsv_range)

	def create_mask(self, img, r):
		hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
		self.data = cv.inRange(hsv, r.low, r.hi)
		self.res = cv.bitwise_and(img,img, mask=self.data)


class ImageMasker:

	masks = []
	color_ranges: list[HSVColorange] = []
	colors: list[HSVColor] = []

	def __init__(self):
		self.img = HSVImg()
		self.color_ranges = []
		self.colors = []

	def run(self)-> list:
		self.create_color_ranges()
		self.create_color_masks()

		# self.save_masks()
		return True

	def create_color_ranges(self):
		# Creates a new color range for each color
		self.color_ranges = []
		for c in self.colors:
			self.color_ranges.append(HSVColorange(c))

	def create_color_masks(self):
		# Creates a new pixel mask for each color
		self.masks = []
		for colorange in self.color_ranges:
			print(
				"creating color mask {} -> {} ".format(
					colorange.low, colorange.hi
				)
			)
			self.masks.append(Mask(self.img.data, colorange))

	def get_mask_data(self)-> list:
		# get the hsv color mask data 
		return [m.data for m in self.masks]

	def save_masks(self)->bool:

		for i, mask in enumerate(self.masks):
			CVImg.save_imgrid(
				mask.res,
				"{}{}.jpg".format(
					self.img.filename,
					str(i)
				)
			)
