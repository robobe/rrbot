import tkinter as Tk
import sys
import os
parent = os.path.dirname(__file__)
sys.path.insert(0, parent)
from models.demo import Model
from views.main_vw import View
import logging

log = logging.getLogger(__name__)

class Controller():
    def __init__(self, event_loop):
        self.event_loop = event_loop
        self.root = Tk.Tk()
        self.model = Model(event_loop)
        self.view = View(self.root)
        self.view.sidepanel.plotBut.bind("<Button-1>",self.__cmd_plot)
        self.model.on_data += self.__data_cb

    def __data_cb(self, data):
        self.view.labelText.set(data)

    def __cmd_plot(self, event):
        self.model.execute_tasks_in_a_new_thread()
        

    def run(self):

        log.info("start controller")
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        # self.model.execute_tasks_in_a_new_thread()
        self.root.mainloop()
        
        # self.view.sidepanel.plotBut.bind("&lt;Button&gt;",self.my_plot)
        # self.view.sidepanel.clearButton.bind("&lt;Button&gt;",self.clear)
 
