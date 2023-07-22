import coloredlogs
import logging
import json

# By default the install() function installs a handler on the root logger,
# this means that log messages from your code and log messages from the
# libraries that you use will all show up on the terminal.
# coloredlogs.install(level='DEBUG')

# If you don't want to see log messages from libraries, you can pass a
# specific logger object to the install() function. In this case only log
# messages originating from that logger will show up on the terminal.
# coloredlogs.install(level='DEBUG', logger=logger)


def get_logger(name, level=logging.DEBUG):
    logger = logging.getLogger(name)
    coloredlogs.install(level=level, logger=logger)

    return logger


def log_object(content):
    return json.dumps(content, indent=4, sort_keys=True)
