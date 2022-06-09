import pygame
import OpenGL.GL as gl
import imgui
import os 

def load_image(image_name='test.png') -> tuple[pygame.Surface,int,int]:
    surface = pygame.image.load(os.path.abspath(image_name))
    textureSurface = pygame.transform.flip(surface, False, True)

    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)

    width = textureSurface.get_width()
    height = textureSurface.get_height()
    texture_id = gl.glGenTextures(1)
    
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, width, height, 0, gl.GL_RGBA,
                    gl.GL_UNSIGNED_BYTE, textureData)

    return texture_id, width, height, surface


class ImageData: # An Image, loaded as a gl texture, able to be rendered in imgui with show()

    texture: int
    surface: pygame.Surface
    img_ID_counter: int = 0000
    imgID: int

    def __init__(self, path):
        global img_ID_counter
        img_ID_counter += 1
        self.imgID = ImageData.img_ID_counter

        self.new_img(path)
        self.loaded = False
        self.failed = False

    def load(self):
        try:
            if not self.loaded:
                self.texture, self.w, self.h, self.surface = load_image(self.path) # Loads the image
            # self.set_width(500)
        except:
            print("Couldn't Load", os.path.abspath(str(self.path)))
            self.failed = True
            return False

        if self.texture:
            self.loaded = True

    def new_img(self, path):
        self.path = path

    def set_width(self, w):
        # Scale to the window
        ratio = self.h / self.w
        self.w = w
        self.h = w * ratio

    def get_dimensions(self):
        #self.load()
        return self.h, self.w

    def show(self):
        if not self.failed and not self.loaded:
            self.load()
        if self.loaded:
            return imgui.image_button(self.texture,self.w, self.h, border_color=(1,1,1,1))

        return False
