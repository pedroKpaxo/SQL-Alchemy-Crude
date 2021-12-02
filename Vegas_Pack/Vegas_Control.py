
from tkinter import filedialog, messagebox,ttk
from types import FunctionType
from Vegas_Pack.Vegas_Model.DB import DataBase
from Vegas_Pack.Vegas_View.viewVegas import App



class Controller():
    """"
    The controller connects the VIew with the Model.
    I'ts the brain, so to speak.

    All the view iniciation and data comes from here.
        This includes the QV_Window
    """

    Model: DataBase
    View: App

    def __init__(self, Model: DataBase, View: App):
        '''
        This function is for controller object
        merging both the Model, with the data,
        and the View with the tkinter elemnts
        '''
        # - Receiving the __init__ data
        self.Model = Model
        self.View = View

    #################

    def Run_App(self):
        '''
        This function is for the main TK object,
        setting up the widgets, and running the mainLoop_App.
        '''
        self.View.Setup_App(self)  # - Pack the widgets

        self.updateTree()       

        self.View.Loop_App()  # - the main Loop_App

    ###############################
    ##                          ###
    ## BLOCK OF EXTRA FUNCTIONS ###
    ##                          ###
    ## ############################

    def send(self,*args):
        '''
        Main Function to add entry data to the database.
        '''
        t= self.View.entry1.e1.get()
        data = {"TASK":t}
        # - Send the data to the database
        self.Model.create(data)
        # - Clears the main treeview
        self.Clear_Tree(self.View.Tree.Tree)
        # - Updates the treeview
        self.updateTree()
        # - Clears the entry
        self.View.entry1.clear()


    def deleterecord(self,*args,**kargs):
        '''
        Function for updating an given record
        '''
        # select the model
        v = self.View.Tree.Tree.item(self.View.Tree.Tree.focus(),'values')
        self.Model.queryName(f'{v[0]}')
        self.updateTree()

        #print(v[0])
   
    def updateTree(self):
        '''
        Gets all the items and display them in the main tree
        '''

        # - THe main list of objcts
        list_ = self.Model.query

        # - Unpack the data from the list
        data = [ (x.task ,x.date.strftime("%d-%m-%Y %H:%M:%S")) for x in list_]
        # - Prints the data
        print(data)
        # - Clears the tree
        self.Clear_Tree(self.View.Tree.Tree)
        # - Insert the data
        self.View.Tree.TreeInsert(data)

    def Clear_Tree(self,tree:ttk.Treeview):
        '''
        Function to clear a given Treeview
        '''
        tree.delete(*tree.get_children())

