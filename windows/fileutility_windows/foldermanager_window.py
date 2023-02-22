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

    label = "Folder looker"

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
        else:
            self.folderdata[path].scan()
        self.selection.set_folder(self.folderdata[path])
        print(f"focus_folder {self.selection.folder.path}")

    def clicked_toolbar(self, signal:int=None):
        if signal is not None:
            if signal == BTN_UP_FOLDER:
                self.focus_folder(
                    # set to directory of file
                    os.path.dirname(self.selection.folder.path)
                )

    def clicked_folder(self, folder: FolderItem=None):
        if folder is not None:
            if folder.is_dir:
                self.focus_folder(folder.path)
            if folder.is_file and folder.is_img:
                self.image_win.replace_image(folder.path)
    DISPLAY_SIGNALS = (True, True)
    def show(self):
        self.DISPLAY_SIGNALS = imgui.begin(self.label, self.DISPLAY_SIGNALS)
        self.clicked_toolbar(self.toolbar.show())
        self.clicked_folder(self.selection.folder.show())
        imgui.end()

        return self.DISPLAY_SIGNALS[1] # signal for close button
