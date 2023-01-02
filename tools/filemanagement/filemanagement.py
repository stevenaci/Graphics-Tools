from xml.sax.handler import property_declaration_handler
import imgui
import os

DIR_ITEM_ENTER = 1

# An Item in the file system
class FolderItem():
    path: str = None
    entry: os.DirEntry = None
    selected: bool = False # gui 

    def __init__(self, entry: os.DirEntry) -> None:
        self.entry = entry
        self.path = entry.path
        pass

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

# File seletion
class Selection():
    folder: FolderData
    def __init__(self) -> None:
        pass
    def set_folder(self, f: FolderData):
        self.folder = f
