import numpy as np
import imgui

def draw_circle(self, r=1):
    # Create an array of theta values from 0 to 2*pi
    theta = np.linspace(0, 2 * np.pi, 8)

    # Calculate the x and y coordinates for each point on the circle
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Combine x and y into a list of tuples
    points = list(zip(x, y))
    self.draw_list.add_polyline(points, imgui.get_color_u32_rgba(1,1,0,1), flags=imgui.DRAW_NONE, thickness=3)
