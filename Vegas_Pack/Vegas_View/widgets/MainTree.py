from tkinter import ttk
import tkinter as tk
from tkinter.constants import END, N


class MainTree(tk.Frame,):
    """
     This class is responsible for the main 'APP' so to speak.

     The MasterFrame_BTN packs the funcionality,

     ANd the treview here is for showing the files that are saved in the 'POOL'.
    """

    def __init__(self,container:tk.Tk,):
        super().__init__(container)
        
        self.s = ttk.Style(self)
        self.background_light= 'gray97'
        self.s.configure('TFrame', background=self.background_light)
        # - Space configuration
        paddings = {'padx': 5, 'pady': 5}

        self.Tree = ttk.Treeview(self,columns=('Task','Date created') ,show='headings',)
        self.Tree.column("#1",minwidth=50 ,width=200)
        self.Tree.heading('#1', text="Task",)
        self.Tree.column("#2",minwidth=50 ,width=200)
        self.Tree.heading('#2', text="Date created",)
        self.Tree.pack(expand=1,fill=tk.BOTH)

    def TreeInsert(self,data):
        print(data)
        for x in data:
            
            self.Tree.insert('',END,values=(x[0],x[1]))
    
        









