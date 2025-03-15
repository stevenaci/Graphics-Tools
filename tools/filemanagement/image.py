from PIL import Image
import OpenGL.GL as gl
import imgui
import os 

def load_image(filename='test.png'):

    image = Image.open(filename)
    image = image.rotate(180)

    width, height = image.size
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, width, height, 0, gl.GL_RGBA,
                    gl.GL_UNSIGNED_BYTE, image.convert("RGBA").tobytes("raw", "RGBA", 0, -1))

    return texture_id, width, height


class ImageData:
    """
    # An Image, loaded as a gl texture, able to be rendered in imgui with show()
    # 
    # """

    texture: int
    #surface: Image.Surface
    img_ID_counter: int = 0000
    imgID: int

    def __init__(self, path):
        global img_ID_counter
        ImageData.img_ID_counter += 1
        self.imgID = ImageData.img_ID_counter

        self.path = path
        self.loaded = False
        self.failed = False

    def load(self):
        try:
            if not self.loaded:
                self.texture, self.w, self.h = load_image(self.path) # Loads the image

        except:
            print("Couldn't Load", os.path.abspath(str(self.path)))
            self.failed = True
            return False

        if self.texture:
            self.loaded = True

    def scale_to_width(self, w):
        ratio = self.h / self.w
        self.w = int(w)
        self.h = int(w * ratio)

    def get_dimensions(self):
        return self.h, self.w

    def show(self):
        if not self.failed and not self.loaded:
            self.load()
        if self.loaded:
            return imgui.image_button(self.texture,self.w, self.h, border_color=(1,1,1,1))

        return False
