import numpy as np
from typing import List
from imgui import Vec2
from tools.art.cv_img import CVImg


def combine_images_from_paths(canvas: Vec2, paths: List[str]):
	imgs = []
	for p in paths:
		imgs.append(CVImg.load_file(p))
	return combine_images(canvas, imgs)


def combine_images(canvas: Vec2, cv_imgs: list):

	surface = CVImg.create_blank_image(canvas.x, canvas.y)
	for img in cv_imgs:
		pix = CVImg.resize_image(img, canvas)
		surface = CVImg.blit(surface, pix)
	return surface
