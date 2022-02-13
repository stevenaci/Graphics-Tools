import pygame
import OpenGL.GL as gl
import imgui
import os 

def load_image(image_name='test.png'):
    image = pygame.image.load(os.path.abspath(image_name))
    textureSurface = pygame.transform.flip(image, False, True)

    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)

    width = textureSurface.get_width()
    height = textureSurface.get_height()
    texture = gl.glGenTextures(1)
    
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, width, height, 0, gl.GL_RGBA,
                    gl.GL_UNSIGNED_BYTE, textureData)

    return texture, width, height

imgID = 0000
class ImageData: # An Image, loaded as a gl texture, able to be rendered in imgui with show()

    def __init__(self, path):
        global imgID
        imgID += 1
        self.imgID = imgID

        self.new_img(path)
        self.loaded = False
        self.failed = False

    def load(self):
        try:
            self.texture, self.w, self.h = load_image(self.path) # Loads the image
            # self.set_width(500)
        except:
            print("Couldn't Load", os.path.abspath(str(self.path)))
            self.failed = True
            return False
            
        if self.texture:
            self.loaded = True
            return True

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
        if not self.failed:
            self.load()
        if self.loaded:
            return imgui.image_button(self.texture,self.w, self.h, border_color=(1,1,1,1))

        return False

