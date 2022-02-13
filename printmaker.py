
from windows.fileutility_windows.foldermanager_window import FolderManagerWindow
from windows.art_windows.image_window import ImageWindow
from Program import Program
from windows.art_windows.masking_window import MaskWindow
from tools.art.Masking import ImageMasker
from windows.art_windows.create_window import CreateWindow

class PrintWindows:

    @staticmethod
    def create():
        print("Generating windows for Art Program")
        im = ImageWindow()
        fm = FolderManagerWindow("/", im)
        masker = ImageMasker()
        ma = MaskWindow(im, masker)
        cw = CreateWindow(iw=im, masker= masker)
        return [fm, im, ma, cw]

class PrintMaker(Program):

    def __init__(self):
        super(Program, self).__init__()
        self.load_windows(
            PrintWindows.create()
        )

if __name__ == "__main__":

    program = PrintMaker()
    program.main()
