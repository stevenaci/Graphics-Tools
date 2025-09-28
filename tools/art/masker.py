from tools.art.cv_image import CVImg
from tools.art.colors.colors import HSVColor, HSVColorange
from tools.art.mask import Mask
from window import gt_window
from window.image_viewer_window import ImageViewerWindow

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
	def timestamped(x: str):
		import time
		return "{}_{}".format(time.time(), x)
	
	# save all masks generated from a file
	def save_masks(self, masks: list[Mask], filename)->bool:
		
		saved_files: list[str] = []
		for i, mask in enumerate(masks):
			saved_files.append("{}-{}.jpg".format(filename, mask.hsv.hi[0]))
			CVImg.save(mask.res, saved_files[-1])

		# save the combined mask
		CVImg.save(
			Mask.combine([m.res for m in masks]), "{}.jpg".format(ImageMasker.timestamped("full"))
		)
		gt_window.window_manager.windows.append(
			ImageViewerWindow(saved_files[-1])
		)


global_masker = ImageMasker()