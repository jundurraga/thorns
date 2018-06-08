"""Utilities.

"""




import os

from . dumpdb import dumpdb, loaddb, get_store, dump, load
from . maps import map, cache
from . bisection import find_zero

def mkdir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
