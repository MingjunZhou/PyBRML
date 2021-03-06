#!/usr/bin/env python

# http://stackoverflow.com/questions/5134893/importing-python-classes-from-different-files-in-a-subdirectory
# __all__ = ['MyClass01','MyClass02']

import variable
import utils
import Potential
import Graph
import Inference

__all__ = ['variable',
           'utils',
           'Potential',
           'Graph',
           'Inference']

if __name__ == "__main__" and __package__ is None:
        __package__ = "brml"
