import imgui
from tools.art.cv_image import CVImg
from windows.art_windows.image_window import ImageWindow
from windows.art_windows.arrange_window import ArrangeWindow
from tools.art.Combining.combine import combine_images, combine_images_from_paths
from tools.art.drawplane import DrawPlane
from tools.art.Masking.masker import global_masker, ImageMasker

class CreateWindow():
    label = "Create window"

    out_sz = 300, 300 # size of output image
    output_name = "TEST"

    combine_masks = None
    masker: ImageMasker

    def __init__(self, aw:ArrangeWindow=None, iw: ImageWindow=None):
        self.aw= aw
        self.iw = iw
        self.masker = global_masker
        self.btn_combine = False
        self.btn_masks = False

        self.drawPlane = DrawPlane((int(self.out_sz[0]), int(self.out_sz[1])))

    def combine_masks(self):
        if self.masker.masks:
            result = combine_images(
                self.drawPlane.dim, 
                self.masker.get_mask_data()
            )
            CVImg.save(
                result,
                "./output/" + "combine_mask" + ".png"
            )

    def combine_imgs(self):
        paths = self.aw.gen_random_imgs()
        result = combine_images_from_paths(self.drawPlane.dim, paths)
        CVImg.save(result, f"./output/{self.output_name}.png")

    def show(self):

        imgui.begin(self.label)

        # OUTPUT TITLE
        changed, self.output_name = imgui.input_text(
            'Filename:', self.output_name, 256)

        # SIZE MODIFIER 
        changed, self.out_sz = imgui.input_float2(
            'Output size  ', *self.out_sz)
        if changed:
            self.drawPlane = DrawPlane(
                (int(self.out_sz[0]), int(self.out_sz[1]))                 
            )

        # COMBINE BTN
        self.btn_combine = imgui.button("Combine Images")
        if self.btn_combine: self.combine_imgs()

        self.btn_masks = imgui.button("Combine Masks")
        if self.btn_masks: self.combine_masks()

        imgui.end()
        return True
