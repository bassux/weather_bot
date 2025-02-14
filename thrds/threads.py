from threading import Thread


def new_thread(func):
    """
    Decorator start func in new thread.
    """

    def wrapper(*args_, **kwargs_):
        new_thread_ = Thread(target=func, args=args_, kwargs=kwargs_, daemon=True)
        new_thread_.start()

    return wrapper
