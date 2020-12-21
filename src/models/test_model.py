import sys
import os
parent = os.path.dirname(__file__)
sys.path.insert(0, parent)
import asyncio
from utils.observer import EventHook # pylint: disable=import-error
from utils import Singleton # pylint: disable=import-error
import pygazebo
import threading
from collections import deque  
import random

MAX_ITEMS = 50

class Model(metaclass=Singleton):

    def __init__(self, event_loop):
        self.on_data = EventHook()
        self.event_loop = event_loop
        self.data = deque([0 for _ in range(50)], MAX_ITEMS)

    
    def get_data(self):
        x = random.randint(1, 10)
        self.data.append(x)
        return list(self.data)

    def cb(self, data):
        imu = pygazebo.msg.imu_pb2.IMU()
        imu.ParseFromString(data)
        print(imu)
        


    async def sub(self):
        manager = await pygazebo.connect()
        subscriber = await manager.subscribe(
            "/gazebo/default/rrbot/link2/link2_imu/imu", 
            'gazebo.msgs.IMU', self.cb)
        

    def execute_tasks_in_a_new_thread(self):
        """ Button-Event-Handler starting the asyncio part. """
        task = asyncio.run_coroutine_threadsafe(self.sub(), self.event_loop)
        # task.add_done_callback(self.got_result)

"""
stamp {
  sec: 373
  nsec: 728000000
}
entity_name: "rrbot::link2"
orientation {
  x: -0.11958728627319103
  y: -5.383447193128897e-07
  z: 4.27013457380437e-07
  w: 0.9928236907736147
}
angular_velocity {
  x: 2.815914364124798e-06
  y: -4.1070917777842356e-05
  z: 3.611843232823096e-05
}
linear_acceleration {
  x: 0.003332424766862567
  y: -2.3274724321458113
  z: 9.519536878963848
}
"""
