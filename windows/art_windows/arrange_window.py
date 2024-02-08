import imgui

from tools.filemanagement.savedata import global_savedata # should be called like "store"..
from tools.filemanagement.imagelist import ImageList

class ArrangeWindow():
    label = "Arrangement"
    img_lists = list[ImageList] #
    new_list_name = ""

    del_img_lists = [] # to destroy on next cycle

    # buttons
    save_lists = False
    create_list = False
    
    def __init__(self):
        self.pos = imgui.Vec2(770, 10)
        self.img_lists: list[ImageList]= [] #
        self.load()
        pass

    def new_imglist(self, label:str, urls:list):
        print(label)
        a = ImageList(label, urls)
        self.img_lists.append(a)

    def gen_random_imgs(self):
        # Returns random selections from each image list,
        # and the placement frame for each.
        paths = []
        for li in self.img_lists:
            paths.append(li.select_random())
        return paths

    def destroy_cycle(self):
        i = 0

        for x in set(self.del_img_lists):
            try:
                self.img_lists.remove(x)
            except ValueError:
                pass
            # if self.img_lists[i] == x:
            #     del self.img_lists[i]
        self.del_img_lists.clear()

    def show(self):
        self.destroy_cycle()

        #imgui.set_next_window_position(self.pos.x, self.pos.y)

        imgui.begin(self.label, flags=imgui.WINDOW_NO_SAVED_SETTINGS)
        _changed, self.new_list_name = imgui.input_text(
        '',        self.new_list_name,        256        )
        imgui.same_line()
        self.create_list = imgui.button("New List")
        if self.create_list:
            self.new_imglist(self.new_list_name, [])

        self.show_img_lists()

        imgui.end()
        return True

    def show_img_lists(self):
        self.save_lists = imgui.button("Save Lists")
        if self.save_lists:
            self.save()
        for b in self.img_lists:
            if b.show() == ImageList.SIG_DEL:
                self.del_img_lists.append(b) # 

    def load(self):

        # dict of saved img strs
        imglists = global_savedata.get_data("imglists") or {}
        
        for label in imglists.keys():
            # take saved strs and recreate image lists
            self.new_imglist(label, imglists[label])


    def save(self):
        # save everything for the window to reload
        print("saving image lists")
        data = {}
        for imglist in self.img_lists:
            data[imglist.label] = imglist.get_img_urls()

        global_savedata.update_data("imglists", data)
        global_savedata.save() # save out
        pass