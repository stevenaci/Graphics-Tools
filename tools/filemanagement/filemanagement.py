import imgui
import os

DIR_ITEM_ENTER = 1

# File seletion
class Selection(): 
    def __init__(self) -> None:
        pass
    def set_folder(self, f):
        self.folder = f
    def set_file(self, f):
        self.file = f

# An Item in the file system
class FolderItem():
    path = None
    entry = None # os.DirEntry
    selected = False # gui 

    def __init__(self, entry: os.DirEntry) -> None:
        self.entry = entry
        self.isdir = entry.is_dir()
        self.isfile = entry.is_file()
        self.isimg = True if entry.path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')) else False
        self.path = entry.path
        pass

    def show(self) -> int:
        if imgui.selectable(self.entry.name)[1]:
            return DIR_ITEM_ENTER

# A folder representation
class FolderData():
    path = None
    contents = dict[str, FolderItem] # FolderItems

    def __init__(self, path:str) -> None:
        self.path = path
        self.scanned = False
        self.scan()

    def scan(self) -> None:
        # scan directory
        #if file: File()
        #if Folder: Folder()
        self.contents = {} # FolderItems
        for e in os.scandir(self.path): # e : os dir entry
            self.contents[e.path] = FolderItem(e)

        self.scanned = True


    def show(self):
        for k, v in self.contents.items():
            if v.show():
                return v
