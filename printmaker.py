from program import Program
from windows.foldermanager_window import FolderManagerWindow
from windows.image_viewer_window import ImageViewerWindow
from windows.masking_window import MaskWindow

class PrintWindows:

    @staticmethod
    def create_windows():
        print("Generating windows for Printmaker Program.")
        im = ImageViewerWindow()
        fm = FolderManagerWindow(None, im)
        ma = MaskWindow(im)
        return [fm, im, ma]

class PrintMaker(Program):

    def __init__(self):
        super(Program, self).__init__()
        self.load_windows(
            PrintWindows.create_windows()
        )

if __name__ == "__main__":

    program = PrintMaker()
    program.main()
