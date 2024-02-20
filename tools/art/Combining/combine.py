from typing import List
from imgui import Vec2
from apps.tools.art.cv_image import CVImg
from tools.errors import process_error

def combine_images_from_paths(canvas_shape: Vec2, paths: List[str]):
	imgs = []
	for p in paths:
		imgs.append(CVImg.load_file(p))
	return combine_images(canvas_shape, imgs)


def combine_images(canvas_shape: Vec2, cv_imgs: list):
	try:

		surface = CVImg.create_blank_image(canvas_shape.x, canvas_shape.y)
		for img in cv_imgs:
			pix = CVImg.resize_image(img, canvas_shape)
			surface = CVImg.blit(surface, pix)
		return surface
	except Exception as e:
		process_error("COMBINE IMAGES {} {}".format(canvas_shape, cv_imgs))