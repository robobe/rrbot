import asyncio


class Model():

    def __init__(self, event_loop):
        self.xpoint = 200
        self.ypoint = 200
        self.res = None
        self.event_loop = event_loop

    async def work(self, ):
        print("start")
        await asyncio.sleep(5)
        print("stop")
        return "work done"

    def got_result(self, future):
        print(future.result())

    def execute_tasks_in_a_new_thread(self):
        """ Button-Event-Handler starting the asyncio part. """
        task = asyncio.run_coroutine_threadsafe(self.work(), self.event_loop)
        task.add_done_callback(self.got_result)
