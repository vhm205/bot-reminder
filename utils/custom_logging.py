import coloredlogs
import logging
import logging.handlers
import json

# By default the install() function installs a handler on the root logger,
# this means that log messages from your code and log messages from the
# libraries that you use will all show up on the terminal.
# coloredlogs.install(level='DEBUG')

# If you don't want to see log messages from libraries, you can pass a
# specific logger object to the install() function. In this case only log
# messages originating from that logger will show up on the terminal.
# coloredlogs.install(level='DEBUG', logger=logger)


def setup_logger(name, write_to_file=False):
    level = logging.DEBUG
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if write_to_file:
        logger_file_handler = logging.handlers.RotatingFileHandler(
            "logs/status.log",
            maxBytes=1024 * 1024,
            backupCount=1,
            encoding="utf8",
        )
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        logger_file_handler.setFormatter(formatter)
        logger.addHandler(logger_file_handler)

    coloredlogs.install(level=level, logger=logger)
    return logger


def log_object(content):
    return json.dumps(content, indent=4, sort_keys=True)
