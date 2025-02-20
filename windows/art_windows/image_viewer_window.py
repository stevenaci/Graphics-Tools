import imgui
import tools.filemanagement.image as iu
from tools.misc.update import Lazy
class ImageViewerWindow(Lazy):
    """
    Window that displays an image
    and has several subscribers

    """
    label = "Image Window"
    img = None
    pos = imgui.Vec2(0,0)
    dim = imgui.Vec2(0,0)
    mask_window = None
    fill_type: str = "fullsize"

    def __init__(self):
        super().__init__()
        pass

    def replace_image(self, path:str):
        self.img = iu.ImageData(path)
        self.update_subscribers()

    def get_image(self):
        return self.img

    def update_fill(self):
        if self.fill_type == "fullsize":
            self.img.scale_to_width(imgui.get_window_width())

    def show(self):
        imgui.begin(self.label)
        imgui.begin(self.label)
        if self.img:
            self.img.show()
            imgui.text(self.img.path)
        self.btn_fill = imgui.button(self.fill_type)
        if self.btn_fill:
            self.update_fill()
        imgui.end()
        imgui.end()
        return True