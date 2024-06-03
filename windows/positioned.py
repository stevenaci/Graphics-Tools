from imgui import Vec4

class Positioned():

    def __init__(self, x_=0, y_=0, w_=500, h_=500) -> None:
        self.x, self.y, self.w, self.h = x_, y_, w_, h_

    def get_frame(self) -> Vec4:
        return Vec4(self.x,self.y,self.w,self.h)
    
    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.y = y
    def set_w(self, w):
        self.w = w
    def set_h(self, h):
        self.h = h
