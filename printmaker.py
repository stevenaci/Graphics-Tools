from program import Program
from window import gt_window
from window.folder_window import FolderWindow
from window.image_viewer_window import ImageViewerWindow
from window.masking_window import MaskWindow

class PrintWindows:

    @staticmethod
    def create_windows():
        im = ImageViewerWindow()
        fm = FolderWindow(None, im)
        ma = MaskWindow(im)
        return [fm, im, ma]

class PrintMakerWindow(Program):

    def __init__(self):
        super(Program, self).__init__()
        gt_window.window_manager.windows = PrintWindows.create_windows()
        

if __name__ == "__main__":

    program = PrintMakerWindow()
    program.main()
