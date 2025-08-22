from program import Program
from windows.folder_manager_window import FolderManagerWindow
from windows.image_viewer_window import ImageViewerWindow
from windows.printmaker import PrintMakerWindow

class PrintWindows:

    @staticmethod
    def create_windows():
        print("Generating windows for Printmaker Program.")
        im = ImageViewerWindow()
        fm = FolderManagerWindow(None, im)
        ma = PrintMakerWindow(im)
        return [fm, im, ma]

class PrintMakerWindow(Program):

    def __init__(self):
        super(Program, self).__init__()
        self.load_windows(
            PrintWindows.create_windows()
        )

if __name__ == "__main__":

    program = PrintMakerWindow()
    program.main()
