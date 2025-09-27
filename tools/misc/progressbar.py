import imgui
import numpy as np
class ProgressBar():
    progress = 0.0
    slice_sz = 2
    height = 10

    def __init__(self, progress=0.0):
        self.progress = progress

    def update_progress(self, p = 0.001):
        self.progress = min(self.progress + p, 1)

    def update_relative(self):
        w_pos = imgui.get_window_position()
        self.xy = imgui.get_cursor_position()
        
        self.xy = imgui.Vec2(self.xy.x + w_pos.x, self.xy.y + w_pos.y) 
        self.height = imgui.get_text_line_height()
        self.width = imgui.get_window_width() # Line width
        self.slice_sz = 2 # Glyph width

    def show(self):
        self.draw_list = imgui.get_window_draw_list()
        self.update_relative()
        slices = int((self.width / self.slice_sz) * self.progress)
        for s in range(slices):
            slice_x, slice_y = (s * self.slice_sz) + self.xy.x , self.xy.y

            self.draw_list.add_rect_filled(
                slice_x,
                slice_y, 
                slice_x + self.slice_sz,
                slice_y + self.height,
                imgui.get_color_u32_rgba(0.0, 0.0, 1.0, 1.0) if s % 2 else imgui.get_color_u32_rgba(0.0, 0.8, 0.3, 1.0)
            )

class InfiniteProgressBar(ProgressBar):
    def update_progress(self, p = 0.001):
        ProgressBar.update_progress(self)
        if self.progress == 1:
            self.progress = 0