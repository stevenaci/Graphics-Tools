import imgui
from tools.art._imageutil import ImageData
from windows.art_windows.image_window import ImageWindow
from windows.art_windows.arrange_window import ArrangeWindow, ImageList

class ImageSelection():
    def __init__(self):
        pass
    def on_delete(self):
        self.imd.imgID

class SelectionWindow():
    name = "Image Window"
    iw = None
    aw:ArrangeWindow  = None

    def __init__(self, iw:ImageWindow, aw:ArrangeWindow):
        self.iw = iw
        self.aw= aw

    def add_to_arrange_list(self, il:ImageList, s:ImageData):
        il.add_img(s) # add the ImageData to the arrange list

    def clear_selection(self, s:ImageData):
        self.iw.remove_image()
        # clean up lists where the image was being used.
        for y in self.aw.img_lists:
            y.remove_if_found(s.imgID)

    def show(self):

        select = self.iw.get_image()

        imgui.set_next_window_position(self.iw.pos.x , self.iw.pos.y + self.iw.dim.y )
        imgui.set_next_window_size(self.iw.dim.x, self.iw.dim.y/2 )
        imgui.begin("Add to Lists")
        if select:
            imgui.text(select.path)
            imgui.text("add to list")
            
            if self.aw:
                # 'add to list' menu
                clicked, n = imgui.combo(
                "", 0, [alist.label for alist in self.aw.img_lists])
                if clicked:
                    self.add_to_arrange_list(self.aw.img_lists[n] , select)


        imgui.end()
        return True