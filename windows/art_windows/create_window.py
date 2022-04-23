import imgui
from tools.art.cv_img import CVImg
from windows.art_windows.image_window import ImageWindow
from windows.art_windows.arrange_window import ArrangeWindow
from tools.art.Combining.combine import combine_images, combine_images_from_paths
from tools.art.drawplane import DrawPlane
from tools.art.Masking.masker import ImageMasker

class CreateWindow():
    label = "Create window"

    out_sz = 300, 300 # size of combine output
    output_name = "TEST"

    on_combine_masks = None
    masker: ImageMasker

    def __init__(self, aw:ArrangeWindow=None, iw: ImageWindow=None, masker: ImageMasker=None):
        self.aw= aw
        self.iw = iw
        self.masker = masker
        self.btn_combine = False
        self.btn_masks = False

        self.drawPlane = DrawPlane(
            (int(self.out_sz[0]), int(self.out_sz[1]))
        )

    def on_combine_masks(self):
        if self.masker.run():
            
            result = combine_images(
                self.masker.img.data, 
                [self.masker.get_mask_data()]
            )
            CVImg.save(
                result,
                "./output/" + "mask_" + self.masker.img.filename + ".png"
            )

    def on_combine_imgs(self):
        #
        paths = self.aw.gen_random_imgs() # the path for each image
        result = combine_images_from_paths(
            self.drawPlane.dim, paths
        )
        CVImg.save(
            result, 
            "./output/" + self.output_name + ".png"
        )

    def show(self):

        imgui.begin(self.label)

        # OUTPUT TITLE
        changed, self.output_name = imgui.input_text(
            'Filename:',
            self.output_name,
            256)

        # SIZE MODIFIER 
        changed, self.out_sz = imgui.input_float2(
            'Output size  ',
             *self.out_sz)
        if changed:
            self.drawPlane = DrawPlane(
                (int(self.out_sz[0]),
                 int(self.out_sz[1]))                 
            )

        # COMBINE BTN
        self.btn_combine = imgui.button("Combine Images")
        if self.btn_combine:
            self.on_combine_imgs()

        self.btn_masks = imgui.button("Combine Masks")
        if self.btn_masks:
            self.on_combine_masks()

        imgui.end()
        return True
