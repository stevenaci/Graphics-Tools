import imgui
import os
from .savedata import global_savedata



DIR_ITEM_ENTER = 1

class File():
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
class Folder():
    path = None
    contents: dict[str, File]={} # FolderItems

    def __init__(self, path:str) -> None:
        self.path = path
        self.contents = self.scan(self.path)

    def show(self):
        for k, v in self.contents.items():
            if v.show():
                return v
    def scan(self, path: str) -> None:
        # refresh contents of directory
        contents = dict()
        try:
            [ contents.update({e.path: File(e)}) for e in os.scandir(self.path)]
            return contents      

        except PermissionError as e:
            print(f"Lacking permissions {e.filename}")

class FolderManager():
    def __init__(self, path=None):
        self.selection = Selection()
        if path:
            self.focus_folder(path)
    
    def load_last_folder(self):
        lastfolder = global_savedata.get('lastfolder')
        if lastfolder:
            try:
                self.focus_folder(lastfolder)
            except FileNotFoundError:
                pass

    def save_last_folder(self):    
        global_savedata.update_data("lastfolder", self.selection.folder.path)
        global_savedata.save() # save out

    def focus_folder(self, path):
        if path not in self.folderdata.keys():
            self.folderdata[path] = Folder(path)
        else:
            self.folderdata[path].scan()
        self.selection.set_folder(self.folderdata[path])
        self.save_last_folder()
        
# File seletion
class Selection():
    folder: Folder
    def __init__(self) -> None:
        self.folder = None
    
    def set_folder(self, f: Folder):
        self.folder = f
