 
from Vegas_Pack import App
from Vegas_Pack import Controller
from Vegas_Pack import DataBase

'''
This is the main door to the application.
'''

if __name__ == "__main__":
    Todo= Controller(DataBase(),App())
    Todo.Run_App()
    