from tools.art.cv_image import CVImg
from tools.art.colors.colors import HSVColor, HSVColorange
from tools.art.Masking.mask import Mask

class ImageMasker:
	"""
		- Load the image masker with colors to be
		masked. 
		- Run the masker to generate a color range and mask it out.
			-- See HSVColorange for ways to configure threshold etc.
	
	"""
	def __init__(self):
		pass

	# Creates a new color range for each color
	def create_color_ranges(self, colors: list[HSVColor]) -> list[HSVColorange]:
		return [HSVColorange(c) for c in colors]

	# Creates a new pixel mask for each color
	def create_color_masks(self, color_ranges: list[HSVColorange], img: CVImg) -> list[Mask]:
		return [Mask(img.data, c) for c in color_ranges]

	def save_masks(self, masks: list[Mask])->bool:
		import time
		for i, mask in enumerate(masks):
			CVImg.save(
				mask.res,
				"{}_{}.jpg".format(
					time.time(),
					str(i)
				))

global_masker = ImageMasker()