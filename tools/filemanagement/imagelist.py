import imgui
from tools.filemanagement.image import ImageData
from random import choice
class ImageList():
    """
        a window used for making lists:

        - Create labelled lists out of urls,
        - Return a random image
        - Retain a size for all images in the list
    """
    imgs = dict[int, ImageData]
    label = ""
    
    SIG_DEL = 1
    def __init__(self,label, urls:list):

        self.label = label

        self.imgs = {}
        for u in urls:
            x = ImageData(u)
            self.add_img(x)
        self.set_color()
        self.del_imgs = []

    def resize(self, w, h):
        self.pos.x = w
        self.pos.y = h


    def select_random(self) -> str:
        imgs = self.get_img_urls()
        return choice(imgs)

    def get_color(self):
        return imgui.get_color_u32_rgba(self.r, self.g, self.b, self.a);

    def add_img(self, img:ImageData):
        self.imgs[img.imgID] = img

    def get_img_urls(self):
        return [x.path for x in self.imgs.values()]

    def remove_if_found(self, id):
        # Remove images if found based on id
        found = False
        self.imgs.pop(id, found)
        return found

    def set_color(self):
        self.r = 0
        self.g = 1
        self.b = 0
        self.a = 0

    def destroy_cycle(self):
        for k in self.del_imgs:
            self.remove_if_found(k)
        self.del_imgs = []

    def show(self):
        _SIG = 0
        self.destroy_cycle()
        # Draw the placement in the window
        # draw_list.add_rect_filled(self.x, self.y,
        # self.w, self.h, 
        # imgui.get_color_u32_rgba(1,1,0,1))

        # SHOW ASSIGNED COLOUR
        imgui.color_button("Button 1", self.r, self.g, self.b, self.a, 0, 17, 30)
        
        visible = True
        expanded, visible = imgui.collapsing_header(self.label, visible)

        if expanded:

            # # POSITIONING IMAGES
            # c,x = imgui.slider_int(
            #     "X##"+ self.label, self.x,
            #     min_value=0, max_value=self.drawPlane.dim.x
            # )
            # if c: self.set_x(x)

            # c,y = imgui.slider_int(
            #     "Y##"+ self.label, self.y,
            #     min_value=0, max_value=self.drawPlane.dim.y
            # )
            # if c: self.set_y(y)

            # c,w = imgui.slider_int(
            #     "W##"+ self.label, self.w,
            #     min_value=0, max_value=self.drawPlane.dim.x
            # )
            # if c: self.set_w(w)

            # c, self.h = imgui.slider_int(
            #     "H##"+ self.label, self.h,
            #     min_value=0, max_value=self.drawPlane.dim.y
            # )

            # Draw the list in a menu
            current = 0
            #imgui.listbox(self.label, current, )

            for id, path in self.imgs.items():
                imgui.text(path.path)
                del_img = imgui.button("remove image")
                if del_img:
                    self.del_imgs.append(id)
            del_list = imgui.button("Erase List.")
            if del_list:
                _SIG = self.SIG_DEL

        return _SIG