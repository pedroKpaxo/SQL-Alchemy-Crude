from tkinter import ttk
from tkinter.constants import NSEW, W

class EntrySimple(ttk.Frame):
    def __init__(self,container) -> None:
        super().__init__(container)
        self.config(width=300)
        self.l1= ttk.Label(self, text="Enter Task").grid(row=0)
        

        self.e1 = ttk.Entry(self)
        

        self.e1.grid(row=0, column=1)
        
        self.BTN_send = ttk.Button(self,text='Send',)
        self.BTN_send.grid(row=0,column=2,rowspan=2,sticky=NSEW,)
        
        self.pack

    def clear(self):
        '''
        Clears the entry data after submission
        '''
        self.e1.delete(0,'end')
        