import logging
import logging.config
import codecs
import json
import os
from controllers import main_ctl

def main():
    logger = logging.getLogger()
    logger.info("This is an INFO message on the root logger.")
    

if __name__ == "__main__":
    # create an initial logger. It will only log to console and it will disabled
    # when we read the logging configuration from the config file.
    # This logger can be useful when we need early logging. E.g. we may want to log
    # the location of the JSON file (e.g. if we get it from a CLI argument).
    logging.basicConfig(level="INFO")
    logger = logging.getLogger()
    logger.info("This is the logger configured by `logging.basicConfig()`.")
    c = main_ctl.Controller()
    c.run()
    
    # Load the configuration.
    config_file = os.path.dirname(__file__)
    config_file = os.path.join(config_file, "log.json")
    with codecs.open(config_file, "r", encoding="utf-8") as fd:
        config = json.load(fd)

    # Set up proper logging. This one disables the previously configured loggers.
    logging.config.dictConfig(config["logging"])
    main()