import imgui
from windows.art_windows.image_viewer_window import ImageViewerWindow
from windows.art_windows.arrange_window import ArrangeWindow

class ArrangeSelectionWindow():
    label = "Image Window"
    iw = None
    arrage_window: ArrangeWindow  = None

    def __init__(self, iw:ImageViewerWindow, aw:ArrangeWindow):
        self.iw = iw
        self.arrage_window= aw

    def show(self):
        selected_image = self.iw.get_image()
        imgui.set_next_window_position(self.iw.pos.x , self.iw.pos.y + self.iw.dim.y )
        imgui.set_next_window_size(self.iw.dim.x, self.iw.dim.y/2 )
        imgui.begin("Add to Lists")
        if selected_image:
            imgui.text(selected_image.path)
            imgui.text("Add to List")
            if self.arrage_window:
                # 'add to list' menu
                clicked, n = imgui.combo(
                    "",
                    0,
                    [alist.label for alist in self.arrage_window.img_lists])
                if clicked:
                    self.arrage_window.img_lists[n].add_img(selected_image) # add the ImageData to the list
        imgui.end()
        return True