import imgui
from tools.art.cv_image import CVImg
from tools.art.masker import ImageMasker
from tools.filemanagement.filemanagement import Folder
from tools.misc.update import Lazy

from .image_viewer_window import ImageViewerWindow

class PrintWindow(Lazy):
    """
    Window with masking functionality
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
        self.masker = ImageMasker()

    def update(self):
        if self.image_win.img:
            self.hsv_img = CVImg(self.image_win.img.path)
            self.masker.img = self.hsv_img

    def quant_and_save_masks(self, img: CVImg):
        _img, colors = img.color_quantize(3)
        self.masker.save_masks(
            self.masker.create_color_masks(
                self.masker.create_color_ranges(colors), img=_img
            ),
            img.filename
        )

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
            self.quant_all_proofs()

        imgui.end()
