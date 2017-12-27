#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from functools import wraps


def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        log = logging.getLogger(fn.__name__)
        log.debug('Start to run %s' % fn.__name__)
        out = fn(*args, **kwargs)
        log.debug('Finish running %s' % fn.__name__)
        return out
    
    return wrapper


@logger
def loadInitialJson(self, file=''):
    """loads the config json file. Path is where the config files are
    located"""
    print('Load json file completed!')


loadInitialJson('abc')

print
"----------------------------------------------------------------"
