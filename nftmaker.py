
from windows.fileutility_windows.foldermanager_window import FolderManagerWindow
from windows.art_windows.image_window import ImageWindow
from windows.fileutility_windows.selection_window import ArrangeSelectionWindow
from windows.art_windows.arrange_window import ArrangeWindow
from windows.art_windows.create_window import CreateWindow
from Program import Program

class NFTWindows:

    @staticmethod
    def create():
        print("Generating windows for NFT")
        im = ImageWindow( )
        fm = FolderManagerWindow("/", im)
        aw = ArrangeWindow()
        sw = ArrangeSelectionWindow(im, aw)
        cw = CreateWindow(aw)
        return [fm, im, sw, aw, cw]

class NFTMaker(Program):

    def __init__(self):
        super(Program, self).__init__(
            NFTWindows.create()
        )

if __name__ == "__main__":

    program = Program()
    program.main()
