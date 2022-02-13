import imgui

class Inputs():
    inputs = []

    def __init__(self, ) -> None:
        pass

class Button():
    text = ""

    def __init__(self, text, args=None) -> None:
        self.text = text
        pass

    def on_click(self):
        pass

    def show(self):
        self.clicked = imgui.button(self.text)
        if self.clicked:
            self.on_click()
