import imgui
import tools.filemanagement.image as iu
from tools.misc.update import Lazy 
class ImageWindow(Lazy):
    """
    Window that displays an image
    and has several subscribers

    """
    label = "Image Window"
    img = None
    pos = imgui.Vec2(0,0)
    dim = imgui.Vec2(0,0)
    mask_window = None
    _fill: str = "fullsize"
    def __init__(self):
        super().__init__()
        pass

    def replace_image(self, path:str):
        self.img = iu.ImageData(path)
        self.update_subscribers()

    def get_image(self):
        return self.img

    def cycle_fill(self):
        if self._fill == "fullsize":
            self.img.set_width(imgui.get_window_width())

    def show(self):
        imgui.begin(self.label)
        self.btn_fill = imgui.button(self._fill)
        if self.btn_fill:
            self.cycle_fill()
        imgui.begin(self.label)
        if self.img:
            self.img.show()
        self.img_pos = imgui.get_item_rect_min()
        imgui.end()
        imgui.end()
        return True