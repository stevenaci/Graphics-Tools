import numpy as np


class HSVColor:

    def __init__(self, hsv: list) -> None:
        self.color = hsv
        pass

    def str_colors(self):
        return f"{self.color[0]}{self.color[1]}{self.color[2]}"

    def get_values(self):
        try:
            return (self.color[0], self.color[1], self.color[2])
        except:
            return 0, 0, 0
    

class HSVColorange:
    # HSV is a method for expressing a color in 3 numbers,
    # each representing the Hue, Saturation, and Value respectively.
    # This generates a range that can be used to create a value mask.
    name = ""
    low = None
    hi = None
    # Saturation/Value pass:
    # Setting this higher extends the lower bound for the
    # saturation and value. If your image is noisy or low-quality this
    # may result in a smoother mask.
    s_pass = 5
    v_pass = 5

    def __init__(self, hsv: HSVColor):
        c = np.array(hsv.color)
        self.low = np.array([c[0]-10, c[1] - self.s_pass, c[2] - self.v_pass])
        self.hi = np.array([c[0]+10, 255, 255])
