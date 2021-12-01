from logging import root
from tkinter import *  
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.constants import BOTH, END, X, Y

from .widgets.MainTree import MainTree
from .widgets.Low_Level_Widgets.Entry import EntrySimple

class App:
    '''
    The main view controller class.

    It Packs all things related to the App Running,
        including the main tk.Tk module.
    '''
 
    def Setup_App(self,Controller):     
        '''
        Starting the main object tk.TK.
        This implementation requires a Controller to be passed along.

        You won't get highlight-text for python synthax, but don't worry,
            it will work!

        The main objective of this implementation is to go hardcore 
            in the modularity of the project, while mantaining the
            MVC design.

        '''
        
        self.MASTER_VEGAS = tk.Tk()
        self.MASTER_VEGAS.option_add('*tearOff', FALSE)
        self.MASTER_VEGAS.title('TODO APP')
        self.MASTER_VEGAS.geometry('800x700')

        ###########################
        # - Start a Menu Bar
        self.MenuBar = Menu(self.MASTER_VEGAS)
        self.MASTER_VEGAS['menu'] = self.MenuBar
        # - add a filemenu to the menu bar
        self.file_menu = Menu(self.MenuBar)
        self.file_menu.add_command(label='Exit',command=self.MASTER_VEGAS.destroy)
        self.MenuBar.add_cascade(label="File",menu=self.file_menu,underline=0)  
        # - Style 
        self.background_light= 'gray97'
        self.Controller = Controller
        ###########################
        
        # - Set the grid layout of the main TK object.
        self.MASTER_VEGAS.grid_rowconfigure(1, weight=1)
        self.MASTER_VEGAS.grid_columnconfigure(1, weight=1,)
        self.MASTER_VEGAS.configure(background=self.background_light)
        #
        # - Create and moutns the widgets.
        self.Create_Widgets()
        #
    
    def Create_Widgets(self):
        '''
        This function allows you to create all the widgetes
            and pack them in the self.MASTER_VEGAS element.
        '''
        self.entry1 = EntrySimple(self.MASTER_VEGAS)
        self.entry1.BTN_send.bind('<Button>',self.Controller.send)
        self.entry1.pack()
        self.Tree = MainTree(self.MASTER_VEGAS)
        self.Tree.pack()
        
        
    

    ######################
    # - VIEW FUNCTIONS - #
    ######################


    def Loop_App(self):
        """"
            Main Loop of the Tk.module
            It is executede by the Controller Module
        """
        self.MASTER_VEGAS.mainloop()



