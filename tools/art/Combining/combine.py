import numpy as np
from typing import List
from imgui import Vec2
from tools.art.Image import _Img


def combine_images_from_paths(canvas: Vec2, paths: List[str]):
	imgs = []
	for p in paths:
		imgs.append(_Img.load_file(p))
	return combine_images(canvas, imgs)


def combine_images(canvas: Vec2, cv_imgs: list):

	surface = _Img.create_blank_image(canvas.x, canvas.y)
	for img in cv_imgs:
		pix = _Img.resize_image(img, canvas)
		surface = _Img.blit(surface, pix)
	return surface
