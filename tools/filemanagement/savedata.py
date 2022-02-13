import pickle
import os

default_save_path= "./savedata/savedata.p"

# try to create a dir
def try_create_dir(path:str):
    try:
        os.mkdir(path)
    except:
        print("\n{} already exists, we didn't create it. ".format(path) )


try_create_dir("./savedata")
try_create_dir("./output")

class SaveData:
    disable_save = False
    data = {}
    def __init__(self, **kargs):
        pass

    def save(self):
        if self.disable_save is False:
            pickle.dump(self.data, open(default_save_path,'wb'))
        pass

    def update_data(self, key, val):
        self.data.update({key: val})

    def append_data(self, key, data):
        v = self.data.get(key)
        if not v or type(v) is not type([]):
            self.data[key] = []
        self.data[key].append(data)

    def clear_data(self,key): 
        self.data[key] = None

    def load(self):
        if not os.path.exists(default_save_path):
            open(default_save_path, 'w').close()
        try:
            self.data = pickle.load(open(default_save_path, "rb" ))
        except EOFError:
            self.data = {}
        print(self.data)

    def get_data(self, key):
        return self.data.get(key)

    def disable_saving(self):
        self.disable_save = True

global_savedata = SaveData()
global_savedata.load()

global_sessiondata = SaveData() # Create "in-data store"