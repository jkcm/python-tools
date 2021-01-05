# -*- coding: utf-8 -*-
"""Some decorators, never know what you'll need...
"""
import datetime as dt
import time

import functools

def timed(func):
    def time_format(t):
        if t>120:
            return f"{t//60}mins "
        elif t>=0.5:
            return f"{round(t,2)}secs"
        elif t*1000>0.5:
            return f"{round(t*1000, 2)}msecs"
        else:
            return f"{round(t*1e6, 2)}nsecs"
    
    
    @functools.wraps(func)
    def timed_decorator(*args, **kwargs):
        start = time.time()
        print(f'{func.__name__}: starting at {time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(start))}.')
        value = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: took {time_format(end-start)}")
        return value
    return timed_decorator