import imgui
import os
from tools.filemanagement.filemanagement import FolderManager, FolderItem, FolderData
from enum import Enum

class FolderManagerToolbar():
    selected = ""

    class Signals(Enum):
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
        if not self.selection.folder:
            self.load_last_folder()
        self.toolbar = FolderManagerToolbar()
        self.image_win = previewwindow
        self.windows = []
        self.DISPLAY_SIGNALS = (True, True)

    def clicked_toolbar(self, signal:int=None):
        if signal is not None:
            if signal == FolderManagerToolbar.Signals.BTN_UP_FOLDER:
                if self.selection.folder:
                    self.focus_folder(os.path.dirname(self.selection.folder.path))
                else:
                    self.focus_folder(os.getcwd())
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
        if self.selection.folder:
          self.clicked_folder(self.selection.folder.show())
        imgui.end()
        return self.DISPLAY_SIGNALS[1] # signal for close button
