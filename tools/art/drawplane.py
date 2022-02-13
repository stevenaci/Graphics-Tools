import imgui

class DrawPlane():

    dim:imgui.Vec2(0,0)

    def __init__(self, dim : tuple):
        self.set_size(dim)

    def set_size(self, dim:tuple):
        self.dim = imgui.Vec2(int(dim[0]), int(dim[1]))

    def get_width(self):
        return self.size.x

    def get_height(self):
        return self.size.h

    def display(self):
        pass


