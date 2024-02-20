from apps.tools.art.cv_image import CVImg
from tools.art.colors.colors import HSVColor, HSVColorange
from tools.art.Masking.mask import Mask

class ImageMasker:
	"""
		- Load the image masker with colors to be
		masked. 
		- Run the masker to generate a color range and mask it out.
			-- See HSVColorange for ways to configure threshold etc.
	
	"""
	masks = []
	color_ranges: list[HSVColorange] = []
	colors: list[HSVColor] = []
	img: CVImg

	def __init__(self):
		self.img = CVImg()
		self.color_ranges = []
		self.colors = []

	def run(self)-> list:
		self.create_color_ranges()
		self.create_color_masks()

		# 
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
			CVImg.save(
				mask.res,
				"{}{}.jpg".format(
					self.img.filename,
					str(i)
				))
