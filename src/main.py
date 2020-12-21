import tkinter as Tk
import logging
import logging.config
import codecs
import json
import os
from controllers import main_ctl    # pylint: disable=import-error
import asyncio
import threading
import di

def main(event_loop):
    logger = logging.getLogger()
    logger.info("load controller")
    root = Tk.Tk()
    # c = main_ctl.Controller(root, event_loop)
    c = di.get_controller(event_loop, root)
    root.title("Tkinter MVC example")
    root.deiconify()
    root.mainloop() 

def start_background_loop(loop: asyncio.AbstractEventLoop) -> None:
    asyncio.set_event_loop(loop)
    loop.run_forever()

if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    logger = logging.getLogger()
    logger.info("Application start")
    
    loop = asyncio.new_event_loop()
    t = threading.Thread(target=start_background_loop, args=(loop,), daemon=True)
    t.start()

    # Load the configuration.
    config_file = os.path.dirname(__file__)
    config_file = os.path.join(config_file, "log.json")
    with codecs.open(config_file, "r", encoding="utf-8") as fd:
        config = json.load(fd)

    logging.config.dictConfig(config["logging"])
    main(loop)