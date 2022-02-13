import cv2 as cv
import numpy as np
from typing import List
from imgui import Vec2
from tools.art.cv_img import CV_IMG


def combine_images_from_paths(canvas: Vec2, paths: List[str]):
	imgs = []
	for p in paths:
		imgs.append(CV_IMG.load_any(p))
	return combine_images(canvas, imgs)

def combine_images(canvas: Vec2, cv_imgs: list):

	surface = CV_IMG.create_blank_image(canvas.x, canvas.y)
	for img in cv_imgs:
		pix = CV_IMG.resize_image(img, canvas)
	surface = CV_IMG.copy_pixels_to_canvas(surface, pix)

	return surface

def test():
		img = CV_IMG.create_blank_image(600, 400)
		img = CV_IMG.resize_image(img, Vec2(400, 300))
		CV_IMG.save_array_img(img, "testimg.png")
		print(img.shape[0])
