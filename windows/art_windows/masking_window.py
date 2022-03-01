import imgui
from tools.art.cv_img import HSVImg
from tools.art.hsvcolors import HSVColor
from tools.art.Masking import ImageMasker
from tools.filemanagement.savedata import global_sessiondata
from tools.misc.update import Update

from windows.art_windows.image_window import ImageWindow



class MaskWindow(Update):
    """
    Window with masking functionality
    Inputs
    - image
    - hsv color
    - outputs a mask of that color range, able to be saved.
    """

    name = "Mask Window"
    img_path: str
    masks = []
    image_win: ImageWindow
    hsv_img: HSVImg
    select_color: HSVColor
    masker: ImageMasker
    btn_add_color = False
    hsv_input = 0, 0, 0
    selecting = False

    def __init__(self, im_win: ImageWindow, masker: ImageMasker):
        self.hsv_img = HSVImg()
        self.masker = ImageMasker()
        self.image_win = im_win

        im_win.add_subscriber(self)

    def update(self):
        if self.image_win.img:
            self.hsv_img = HSVImg(self.image_win.img.path)

    def select_pixel(self):

        if self.hsv_img.load:
            xy = imgui.get_mouse_pos()

            # xy = imgui.Vec2(
            #     xy.x - self.image_win.img_pos.x,
            #     xy.y - self.image_win.img_pos.y
            # )

            self.select_color = HSVColor(
                self.hsv_img.get_pixel(xy)
            )
            self.hsv_input = self.select_color.get_values()

    def add_current_color(self):
        # add a color to mask
        self.masker.colors.append(
            HSVColor(self.hsv_input)
        )

    def gen_masks(self):
        self.masker.img = self.hsv_img
        global_sessiondata.update_data("mask_colors", self.masker.colors)
        self.masker.run()

    def show(self):
        imgui.begin(self.name)
        _, self.hsv_input = imgui.input_int3('HSV', *self.hsv_input)

        self.btn_add_color = imgui.button("Add Colormask")
        if self.btn_add_color:
            self.selecting = True
        if self.hsv_img:
            self.hsv_img.display()
        for hsv in self.masker.colors:
            imgui.text(hsv.str_colors())

        if imgui.is_mouse_down() and self.selecting:
            self.select_pixel()
            self.add_current_color()
            self.selecting = False

        self.btn_gen_masks = imgui.button("Gen Masks")
        if self.btn_gen_masks:
            self.gen_masks()

        imgui.end()
        return
