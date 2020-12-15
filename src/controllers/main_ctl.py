import tkinter as Tk
import sys
import os
parent = os.path.dirname(__file__)
sys.path.insert(0, parent)
from models.demo import Model
from viewsץmain_vw import View

class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root)
    
    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        self.root.mainloop()
        # self.view.sidepanel.plotBut.bind("&lt;Button&gt;",self.my_plot)
        # self.view.sidepanel.clearButton.bind("&lt;Button&gt;",self.clear)
 
