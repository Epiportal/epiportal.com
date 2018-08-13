# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 21:34:21 2017

@author: Nathalie
"""

import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print(f.__name__, 'function tooks',(time2-time1)*1000.0,'ms')
        return ret
    return wrap