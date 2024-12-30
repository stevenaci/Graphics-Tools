import imgui
import os
from .savedata import global_savedata

DIR_ITEM_ENTER = 1

class FolderItem():
# An Item in the file system
    path: str = None
    entry: os.DirEntry = None
    selected: bool = False # gui 

    def __init__(self, entry: os.DirEntry) -> None:
        self.entry = entry
        self.path = entry.path

    @property
    def is_dir(self):
        return self.entry.is_dir()

    @property
    def is_file(self):
        return self.entry.is_file()
    
    @property
    def is_img(self):
        return True if self.entry.path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')) else False

    def show(self) -> int:
        if imgui.selectable(self.entry.name)[1]:
            return DIR_ITEM_ENTER

# A folder representation
class FolderData():
    path = None
    contents: dict[str, FolderItem]={} # FolderItems

    def __init__(self, path:str) -> None:
        self.path = path
        self.scan()

    def scan(self) -> None:
        # refresh contents of directory
        self.contents = dict()
        try:
            for e in os.scandir(self.path): # e : os dir entry
                self.contents[e.path] = FolderItem(e)
        except:
            print("Folder not accessible")

    def show(self):
        for k, v in self.contents.items():
            if v.show():
                return v

class FolderManager():
    folderdata: dict[str, FolderData]
    def __init__(self, path=None):
        self.selection = Selection()
        if path:
            self.focus_folder(path)
    
    def load_last_folder(self):
        lastfolder = global_savedata.get('lastfolder')
        if lastfolder:
            self.focus_folder(lastfolder)
            
    def save_last_folder(self):    
        global_savedata.update_data("lastfolder", self.selection.folder.path)
        global_savedata.save() # save out

    def focus_folder(self, path):
        try:
            if path not in self.folderdata.keys():
                self.folderdata[path] = FolderData(path)
            else:
                self.folderdata[path].scan()
            self.selection.set_folder(self.folderdata[path])
            self.save_last_folder()
        except FileNotFoundError:
            pass

# File seletion
class Selection():
    folder: FolderData
    def __init__(self) -> None:
        self.folder = None
    
    def set_folder(self, f: FolderData):
        self.folder = f
