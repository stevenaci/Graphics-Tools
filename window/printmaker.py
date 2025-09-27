import imgui
from tools.art.cv_image import CVImg
from tools.art.colors.colors import HSVColor
from tools.filemanagement.filemanagement import Folder
from tools.filemanagement.savedata import save_state
from tools.misc.progressbar import InfiniteProgressBar
from tools.art.masker import image_masker, ImageMasker, Mask
from tools.misc.update import Lazy

from windows.image_viewer_window import ImageViewerWindow

class PrintMakerWindow(Lazy):
    """
    Window with masking functionality
    Inputs
    - image
    - hsv color
    - outputs a mask of that color range, able to be saved.
    """
    label = "Mask Window"
    img_path: str
    image_win: ImageViewerWindow
    hsv_img: CVImg

    def __init__(self, im_win: ImageViewerWindow):
        self.hsv_img = CVImg()
        self.image_win = im_win
        self.colors = []
        im_win.add_subscriber(self)

    def update(self):
        if self.image_win.img:
            self.hsv_img = CVImg(self.image_win.img.path)
            self.masker.img = self.hsv_img

    def quant_and_save_masks(self, img: CVImg):
        _img, colors = img.color_quantize(3)
        return self.masker.create_color_masks(image_masker.create_color_ranges(colors), img=_img)

    def quant_all_proofs(self):
        import os
        PROOF_FOLDER = os.getcwd() + "/proofs"
        for file in Folder(PROOF_FOLDER).contents.values():
            self.quant_and_save_masks(CVImg(file.path))

    def show(self):
        imgui.begin(self.label)

        self.btn_color_quant = imgui.button("Color Quantize Mask")
        if self.btn_color_quant:
            self.quant_and_save_masks(self.hsv_img)

        btn_proofs = imgui.button("Quantize all proofs")
        if btn_proofs:
            self.quant_and_save_masks(self.hsv_img)

        imgui.end()
