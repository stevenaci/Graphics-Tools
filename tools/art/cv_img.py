import numpy as np
import cv2 as cv
import os
import imgui
from typing import List


class HSVImg():


	def __init__(self, fn: str=""):
		self.load = False
		self.filename = fn.split(".")[:1][0]
		self.data = None

		if fn is not "":
			self.data = CVImg.load_file(fn)
			self.load = True

	def get_pixel(self, xy: imgui.Vec2):
		if self.load:
			w = self.data.shape[0]
			h = self.data.shape[1]
			x = int(xy.x)
			y = int(xy.y)
			pix = [0, 0, 0]
			if x < w and y < h:
				pix = self.data[x, y]
			return pix
	def display(self):
		if self.load:
			pass # not here yet
			#imgui.image(self.data, height=150, title="flowers")
			#imgui.text_ansi_colored("test")

class CVImg():


	def create_blank_image(w, h):
			# creates a blank drawable surface for opencv
			# alpha
			return np.zeros((w, h, 4), np.uint8)
			# no alpha
			#

	def load_file(fname: str):
			# loads an image in opencv
		img = cv.imread(os.path.abspath(fname), cv.IMREAD_UNCHANGED)
		if img is None:
			print("Couldnt read img : {}".format(fname))

		if len(img[0][0]) < 4:
			print("PNG HAS NO TRANSPARENCY : {}".format(fname))
			print("Top left pixel : {}".format(img[0][0]))
			return img

		return img

	def save_imgrid(grid: np.array, fn) -> bool:
		cv.imwrite(fn, grid)
		print("Saved {}".format(fn))

	def select_pixel(self, img, xy: tuple):
		return img[xy[0],xy[1]]
	
	def resize_image(grid: np.array, dim: imgui.Vec2) -> np.array:
			return cv.resize(grid, (dim.y, dim.x), interpolation=cv.INTER_NEAREST)
	
	def copy_pixels_to_canvas(canvas: np.array, img: np.array):
		yi = 0
		xi = 0

		ymax = canvas.shape[1]
		xmax = canvas.shape[0]
		for y in range(ymax):
			for x in range(xmax):
				canvas[xi][yi][:] = CVImg.add_pixels(canvas[xi][yi][:], img[xi][yi][:])
				xi += 1
			yi += 1
			xi = 0
	
		return canvas

	def clamp(num, min_value, max_value):
			return max(min(num, max_value), min_value)

	def clamp_pixel(pix: np.array):
		try:
			pix[0] = int(CVImg.clamp(pix[0], 0, 255))
			pix[1] = int(CVImg.clamp(pix[1], 0, 255))
			pix[2] = int(CVImg.clamp(pix[2], 0, 255))
			pix[3] = int(CVImg.clamp(pix[3], 0, 255))

		except:
			print("PIXEL CLAMP ERROR:", str(pix))
		return pix

	def weight_add(a, b, bw):
		return (float(a)  * (1.0 - bw)) + float(b) * bw

	def add_pixels(a, b):
		b_alpha = float(b[3])
		alpha_2 = b_alpha / 255.0

		a[0] = CVImg.weight_add(a[0], b[0], alpha_2)
		a[1] = CVImg.weight_add(a[1], b[1], alpha_2)
		a[2] = CVImg.weight_add(a[2], b[2], alpha_2)
		a[3] = CVImg.weight_add(a[3], b[3], alpha_2)

		return CVImg.clamp_pixel(a) # clamp to png values

	def combine_images(canvas: imgui.Vec2, paths: List[str]):

		surface = CVImg.create_blank_image(canvas.x, canvas.y)

		for p in paths:
			img = CVImg.load_any(p)
			if not img.any(): # If image load fails, just return
				return
				
			img = CVImg.resize_image(img, canvas)
			surface = CVImg.copy_pixels_to_canvas(surface, img)

		return surface