
from windows.art_windows.arrange_window import ArrangeWindow
from windows.fileutility_windows.foldermanager_window import FolderManagerWindow
from windows.art_windows.image_window import ImageWindow
from Program import Program
from windows.art_windows.masking_window import MaskWindow
from tools.art.Masking.masker import ImageMasker
from windows.art_windows.create_window import CreateWindow
from windows.fileutility_windows.selection_window import SelectionWindow

class PrintWindows:

    @staticmethod
    def create():
        print("Generating windows for Art Program")
        im = ImageWindow()
        fm = FolderManagerWindow("/", im)
        masker = ImageMasker()
        ma = MaskWindow(im, masker)
        aw = ArrangeWindow()
        cw = CreateWindow(aw=aw, iw=im, masker= masker)
        sw = SelectionWindow(im, aw)
        return [aw, fm, im, ma, cw, sw]

class PrintMaker(Program):

    def __init__(self):
        super(Program, self).__init__()
        self.load_windows(
            PrintWindows.create()
        )

if __name__ == "__main__":

    program = PrintMaker()
    program.main()
