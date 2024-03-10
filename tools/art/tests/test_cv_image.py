from ..cv_image import CVImg

def test_blit_images_():
	w = 100
	h = 100
	img1 = CVImg.create_blank_image(w, h)
	img2 = CVImg.create_blank_image(w, h)
	CVImg.blit(img1, img2)
	assert img1.size == img2.size