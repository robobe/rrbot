import sys
import os
parent = os.path.dirname(__file__)
sys.path.insert(0, parent)
import asyncio
from utils.observer import EventHook
from utils import Singleton

class Model(metaclass=Singleton):

    def __init__(self, event_loop):
        self.on_data = EventHook()
        self.xpoint = 200
        self.ypoint = 200
        self.res = None
        self.event_loop = event_loop
        

    async def work(self):
        print("start")
        await asyncio.sleep(2)
        print("stop")
        return "work done"

    def got_result(self, future):
        result = future.result()
        self.on_data.fire(result)

    def execute_tasks_in_a_new_thread(self):
        """ Button-Event-Handler starting the asyncio part. """
        task = asyncio.run_coroutine_threadsafe(self.work(), self.event_loop)
        task.add_done_callback(self.got_result)
