from tkinter import Tk, Button
import asyncio
import threading

async def work():
    print("start")
    await asyncio.sleep(2)
    print("stop")
    return "work done"

def asyncio_thread(event_loop):
  print('The tasks of fetching multiple URLs begins')
  event_loop.run_until_complete(work())

def execute_tasks_in_a_new_thread(event_loop):
  """ Button-Event-Handler starting the asyncio part. """
  task = asyncio.run_coroutine_threadsafe(work(), event_loop)

def check_if_button_freezed():
  print(
      'This button is responsive even when a list of i/o tasks are in progress'
  )

def start_background_loop(loop: asyncio.AbstractEventLoop) -> None:
    asyncio.set_event_loop(loop)
    loop.run_forever()

def main(event_loop):
    root = Tk()
    
    Button(
        master=root,
        text="hello",
        command=lambda : execute_tasks_in_a_new_thread(event_loop)
    ).pack()

    Button(
        master=root,
        text="hello2",
        command=check_if_button_freezed
    ).pack()

    
    root.mainloop()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    t = threading.Thread(target=start_background_loop, args=(loop,), daemon=True)
    t.start()
    main(loop)
