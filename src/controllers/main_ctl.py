import tkinter as Tk
import sys
import os
parent = os.path.dirname(__file__)
sys.path.insert(0, parent)
from models.demo import Model # pylint: disable=import-error
from views.main_vw import View # pylint: disable=import-error
import logging

log = logging.getLogger(__name__)

class Controller():
    def __init__(self, tk, event_loop):
        self.event_loop = event_loop
        
        self.model = Model(event_loop)
        self.view = View(tk)
        self.view.sidepanel.plotBut.bind("<Button-1>",self.__cmd_plot)
        self.model.on_data += self.__data_cb

    def __data_cb(self, data):
        self.view.labelText.set(data)

    def __cmd_plot(self, event):
        self.model.execute_tasks_in_a_new_thread()
        

    def run(self):

        log.info("start controller")
             
 
