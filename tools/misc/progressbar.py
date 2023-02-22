import imgui

class ProgressBar():

    p_done = 0.0
    slice_sz = 22
    sz = 100.0

    def __init__(self, progress=0.0):
        self.p_done = progress


    def update(self, p = 0.001):
        
        self.p_done = min(self.p_done + p, 100)

    def update_position(self):
        # ALL CALLBACK
        self.xy = imgui.get_window_position()
    def show(self):
        draw_list = imgui.get_window_draw_list()
        self.update_position()
        slices = int(self.sz / self.slice_sz)

        for s in range(slices):
            if s % 2:
                x = s * self.slice_sz
                draw_list.add_rect_filled(
                    x + self.xy.x,
                    self.xy.y, x + self.slice_sz,
                    x +self.slice_sz,
                    imgui.get_color_u32_rgba(0.0, 0.0, 1.0, 1.0)
                )

