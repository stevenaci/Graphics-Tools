# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os
os.environ["PYSDL2_DLL_PATH"] = "./"

from sdl2 import *
import sdl2.ext
import sdl2.ext.particles

import ctypes
import OpenGL.GL as gl

import imgui
from imgui.integrations.sdl2 import SDL2Renderer

from tools.filemanagement.savedata import global_savedata

def to_path(p:str):
    return p.replace('\\','/') 

class Program:

    windows = []

    RESOURCES = sdl2.ext.Resources(__file__, "resources")

    def __init__(self):
        pass
    
    def load_windows(self, wins):
        self.windows = wins

    def display_window(self):

        imgui.begin_group()
        for win in self.windows:
            if win.show() == False:
                self.windows.remove(win)
        imgui.end_group()

    def main(self):
        window, gl_context = self.impl_pysdl2_init()
        imgui.create_context()
        impl = SDL2Renderer(window)

        running = True
        event = SDL_Event()

        #cm.load_images()
        while running:
            while SDL_PollEvent(ctypes.byref(event)) != 0:
                if event.type == SDL_QUIT:
                    running = False
                    break
                impl.process_event(event)
            impl.process_inputs()

            imgui.new_frame()

            if imgui.begin_main_menu_bar():
                if imgui.begin_menu("File", True):

                    clicked_quit, selected_quit = imgui.menu_item(
                        "Quit", 'Cmd+Q', False, True
                    )
                    if clicked_quit:
                        exit(1)
                    imgui.end_menu()

                imgui.end_main_menu_bar()

            #flags = imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE
            flags = imgui.WINDOW_ALWAYS_AUTO_RESIZE
            # WINDOW #
            self.display_window()

            # CLEAR #
            gl.glClearColor(0.3, 0.7, 1., 1)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

            imgui.render()
            impl.render(imgui.get_draw_data())
            SDL_GL_SwapWindow(window)

        # save apps?
        impl.shutdown()
        SDL_GL_DeleteContext(gl_context)
        SDL_DestroyWindow(window)
        SDL_Quit()


    def impl_pysdl2_init(self):
        width, height = 1280, 720
        window_name = "12-3-12301"

        if SDL_Init(SDL_INIT_EVERYTHING) < 0:
            print("Error: SDL could not initialize! SDL Error: " + SDL_GetError())
            exit(1)

        SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1)
        SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24)
        SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 8)
        SDL_GL_SetAttribute(SDL_GL_ACCELERATED_VISUAL, 1)
        SDL_GL_SetAttribute(SDL_GL_MULTISAMPLEBUFFERS, 1)
        SDL_GL_SetAttribute(SDL_GL_MULTISAMPLESAMPLES, 16)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_FLAGS, SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 4)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 1)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE)

        SDL_SetHint(SDL_HINT_MAC_CTRL_CLICK_EMULATE_RIGHT_CLICK, b"1")
        SDL_SetHint(SDL_HINT_VIDEO_HIGHDPI_DISABLED, b"1")

        window = SDL_CreateWindow(window_name.encode('utf-8'),
                                SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                                width, height,
                                SDL_WINDOW_OPENGL|SDL_WINDOW_RESIZABLE)

        if window is None:
            print("Error: Window could not be created! SDL Error: " + SDL_GetError())
            exit(1)

        gl_context = SDL_GL_CreateContext(window)
        if gl_context is None:
            print("Error: Cannot create OpenGL Context! SDL Error: " + SDL_GetError())
            exit(1)

        SDL_GL_MakeCurrent(window, gl_context)
        if SDL_GL_SetSwapInterval(1) < 0:
            print("Warning: Unable to set VSync! SDL Error: " + SDL_GetError())
            exit(1)

        return window, gl_context
