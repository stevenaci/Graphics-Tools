import cv2 as cv
import numpy as np
import os
import imgui
from tools.art.colors.quantization import Quantization
from tools.math import clamp

class CVImg(Quantization):
	"""
	_Img: Image class that combines some libs

	"""
	data: np.array

	def __init__(self, fn: str=""):
		self.load = False
		self.filename = fn.split(".")[:1][0]
		self.data = None

		if fn != "":
			self.data = CVImg.load_file(fn)
			self.load = True
			self.w = self.data.shape[0]
			self.h = self.data.shape[1]

	def get_pixel(self, xy: imgui.Vec2):
		try:

			x = int(xy.x)
			y = int(xy.y)
			pix = [0, 0, 0]
			if x < self.w and y < self.h:
				pix = self.data[x, y]
			return pix
		except:
			return None

	def select_pixel(self, img, xy: tuple):
		return img[xy[0],xy[1]]

	def display(self):
		# imgui.image_button(self.data,0, 0, border_color=(1,1,1,1))
		pass

	def create_blank_image(w, h, alpha=True):
			# creates a blank drawable surface for opencv
			# any 3 int color format -> 255,255,255
			# alpha
			if alpha:
				return np.zeros((w, h, 4), np.uint8)
			return np.zeros((w, h, 3), np.uint8)
			# no alpha
			#

	def load_file(fname: str):
		# loads an image in opencv
		img = cv.imread(os.path.abspath(fname), cv.IMREAD_UNCHANGED)
		if img is None:
			print("Couldnt read img : {}".format(fname))
			return None
		if len(img[0][0]) < 4:
			print("PNG HAS NO TRANSPARENCY : {}\n appending max alpha".format(fname))
			img = np.insert(img, 3, 255, axis=2)
			print(img[0])
		return img


	def save(grid: np.array, fn: str) -> bool:
		outputfolder = "./output/"
		if grid is not None:
			cv.imwrite(outputfolder + fn, grid)
			print(f"Saved to {outputfolder}/{fn}")

	def resize_image(grid: np.array, dim: imgui.Vec2) -> np.array:
			return cv.resize(grid, (dim.y, dim.x), interpolation=cv.INTER_NEAREST)
	
	def blit(dst: np.array, src: np.array, origin = (0,0)):
		"""
			Copy one np array onto another
		"""


		ymax = dst.shape[1]-origin[1]
		xmax = dst.shape[0]-origin[0]
		for y in range(ymax):
			for x in range(xmax):
				dst[x+origin[0]][y+origin[1]] = CVImg.add_pixels_alpha(
					dst[x+origin[0]][y+origin[1]], src[x][y])
		return dst

	def clamp_pixel(pix: np.array): # clamp to 8 bit
		try:
			pix[0] = int(clamp(pix[0], 0, 255))
			pix[1] = int(clamp(pix[1], 0, 255))
			pix[2] = int(clamp(pix[2], 0, 255))
			pix[3] = int(clamp(pix[3], 0, 255))

		except:
			print("PIXEL CLAMP ERROR:", str(pix))
		return pix

	def weight_add(a, b, bw):
		return (float(a)  * (1.0 - bw)) + float(b) * bw

	def add_pixels_alpha(a, b):
		"""
			add pixels that have alpha channels.
		"""
		b_alpha = float(b[3])
		alpha_2 = b_alpha / 255.0

		a[0] = CVImg.weight_add(a[0], b[0], alpha_2)
		a[1] = CVImg.weight_add(a[1], b[1], alpha_2)
		a[2] = CVImg.weight_add(a[2], b[2], alpha_2)
		a[3] = CVImg.weight_add(a[3], b[3], alpha_2)

		return CVImg.clamp_pixel(a) # clamp to png values
