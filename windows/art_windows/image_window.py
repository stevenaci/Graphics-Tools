import imgui
import tools.art._imageutil as iu
from tools.misc.update import Update 
"""
Window that displays an image
and has several subscribers

"""
class ImageWindow(Update):
    name = "Image Window"
    img = None
    pos = imgui.Vec2(0,0)
    dim = imgui.Vec2(0,0)
    mask_window = None

    def __init__(self):
        super().__init__()
        pass

    def replace_image(self, path:str):
        self.img = iu.ImageData(path)
        self.update_subscribers()

    def get_image(self):
        return self.img

    def update_subscribers(self):
        super().update_subscribers()

    def show(self):
        imgui.begin(self.name)
        if self.img:
            self.img.show()

        self.img_pos = imgui.get_item_rect_min()

        imgui.end()
        return True