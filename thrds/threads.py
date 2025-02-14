import threading
from threading import Thread


def new_thread(func):
    """
    Decorator start func in new thread.
    """
    def wrapper(*args_, **kwargs_):
        tr = Thread(target=func, args=args_, kwargs=kwargs_, daemon=True)
        tr.start()

    return wrapper
