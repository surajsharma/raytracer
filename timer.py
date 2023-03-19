import logging
import time

from functools import wraps

logging.basicConfig()
logger = logging.getLogger("my-logger")
logger.setLevel(logging.DEBUG)


def timed(func):
    """This decorator prints the execution time for the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.debug("{} ran in {}s".format(
            func.__name__, round(end - start, 2)))
        return result

    return wrapper
