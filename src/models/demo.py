import sys
import os
parent = os.path.dirname(__file__)
sys.path.insert(0, parent)
import asyncio
from utils.observer import EventHook # pylint: disable=import-error
from utils import Singleton # pylint: disable=import-error
import pygazebo
import threading

class Model(metaclass=Singleton):

    def __init__(self, event_loop):
        self.on_data = EventHook()
        self.event_loop = event_loop
        

    # async def work(self):
    #     print("start")
    #     await asyncio.sleep(2)
    #     print("stop")
    #     return "work done"

    # def got_result(self, future):
    #     result = future.result()
    #     self.on_data.fire(result)

    def cb(self, data):
        poses_stamped = pygazebo.msg.poses_stamped_pb2.PosesStamped()
        poses_stamped.ParseFromString(data)
        self.on_data.fire(poses_stamped.pose[0].position.x) # pylint: disable=maybe-no-member


    async def sub(self):
        manager = await pygazebo.connect()
        subscriber = await manager.subscribe(
            "/gazebo/default/pose/info", 
            'gazebo.msgs.PosesStamped', self.cb)
        

    def execute_tasks_in_a_new_thread(self):
        """ Button-Event-Handler starting the asyncio part. """
        task = asyncio.run_coroutine_threadsafe(self.sub(), self.event_loop)
        # task.add_done_callback(self.got_result)
