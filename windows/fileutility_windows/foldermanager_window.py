import imgui
import os
from tools.filemanagement.filemanagement import FolderItem, FolderData, Selection

BTN_UP_FOLDER = 2

class Toolbar():
    selected = ""

    def __init__(self) -> None:
        pass
    def show(self):
        if imgui.button("Go up"):
            return BTN_UP_FOLDER

class FolderManagerWindow():

    wintitle = "Folder looker"
    x = 0
    y = 100
    w = 50
    h = 400
    DISPLAY_SIGNALS = (True, True)
    handle_callbacks = []

    imgpath = ""
    selection = None
    folderdata = {}

    
    def __init__(self, path=None, previewwindow=None):
        self.toolbar = Toolbar()
        if not path:
            path = os.getcwd()
        self.selection = Selection()
        self.focus_folder(path)
        self.image_win = previewwindow
        pass
   

    def focus_folder(self, path):

        if path not in self.folderdata.keys():
            self.folderdata[path] = FolderData(path)

        self.selection.set_folder(self.folderdata[path])
        print("focus_folder " + self.selection.folder.path)

    def handle_toolbar(self, signal:int=None):
        if signal is not None:
            if signal == BTN_UP_FOLDER:
                self.focus_folder(
                    # set to directory of file
                    os.path.dirname(self.selection.folder.path)
                )

    def handle_folder(self, signal:FolderItem=None):
        if signal is not None:
            if signal.isdir:
                self.focus_folder(signal.path)
            if signal.isfile and signal.isimg:
                self.image_win.replace_image(signal.path)

    def show(self):
        self.DISPLAY_SIGNALS = imgui.begin(self.wintitle, self.DISPLAY_SIGNALS)
        
        self.handle_toolbar(self.toolbar.show())
        
        self.handle_folder(self.selection.folder.show())
        
        imgui.end()

        return self.DISPLAY_SIGNALS[1] # signal for close button
