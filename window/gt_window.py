import imgui

class Window():
    label: str = "DefaultWindow"

    def show(self):
        pass
    
class WindowMananger():
    windows: list[Window]
    def __init__(self):
        self.windows = []

    def display_windows(self):
        imgui.begin_group()
        for win in self.windows:
            if win.show() == False:
                self.windows.remove(win)
        imgui.end_group()

window_manager = WindowMananger()