import imgui
import os
from tools.filemanagement.filemanagement import FolderManager, FolderItem, FolderData, Selection

class FolderManagerToolbar():
    selected = ""

    class Signals(enum):
        BTN_NEW_WINDOW = 1
        BTN_UP_FOLDER = 2
    
    def __init__(self) -> None:
        pass
    def show(self):
        if imgui.button("Go up"):
            return self.Signals.BTN_UP_FOLDER

class FolderManagerWindow(FolderManager):

    label = "Folder looker"

    imgpath = ""
    selection = None
    folderdata = {}

    
    def __init__(self, path=None, previewwindow=None):
        FolderManager.__init__(self, path)

        self.toolbar = Toolbar()
        self.image_win = previewwindow
        self.windows = []
        self.DISPLAY_SIGNALS = (True, True)
   

    def focus_folder(self, path):
        if path not in self.folderdata.keys():
            self.folderdata[path] = FolderData(path)
        else:
            self.folderdata[path].scan()
        self.selection.set_folder(self.folderdata[path])
        print(f"focus_folder {self.selection.folder.path}")

    def clicked_toolbar(self, signal:int=None):
        if signal is not None:
            if signal == FolderManagerToolbar.Signals.BTN_UP_FOLDER:
                self.focus_folder(os.path.dirname(self.selection.folder.path))
            if signal == FolderManagerToolbar.Signals.BTN_NEW_WINDOW:
                self.open_new_window(self.selection.folder.path)

    def clicked_folder(self, folder: FolderItem=None):
        if folder is not None:
            if folder.is_dir:
                self.focus_folder(folder.path)
            if folder.is_file and folder.is_img:
                self.image_win.replace_image(folder.path)


    def open_new_window(self, path):
        self.windows.append(FolderManagerWindow(path, self.image_win))

    DISPLAY_SIGNALS = (True, True)
    def show(self):
        
        self.DISPLAY_SIGNALS = imgui.begin(self.label, self.DISPLAY_SIGNALS)
        self.clicked_toolbar(self.toolbar.show())
        # print(len(self.selection.folder.contents))

        self.clicked_folder(self.selection.folder.show())
        imgui.end()
        return self.DISPLAY_SIGNALS[1] # signal for close button
