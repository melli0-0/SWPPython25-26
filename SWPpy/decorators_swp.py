import time
from functools import wraps

def measure_runtime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        elapsed_time = end - start
        print (f"{func.__name__} - elapsed time = {elapsed_time}")
        return output
    return wrapper

