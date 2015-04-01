from abc import ABCMeta, abstractmethod
from queue import Queue

class StackLayer(object):
    __metaclass__ = ABCMeta

    def __init__(self, below_queue):
        self.above_queue = Queue()
        self.below_queue = below_queue
        
    @abstractmethod
    def pass_down (self):
        raise Exception('pass_down is not implemented!')
