from abc import ABCMeta, abstractmethod
from queue import Queue
import threading

class StackLayer(object):
    __metaclass__ = ABCMeta

    def __init__(self, below_queue):
        self.above_queue = Queue()
        self.below_queue = below_queue
        
        thread = threading.Thread(target=self.receive)
        thread.start()
        
    @abstractmethod
    def pass_down (self):
        raise Exception('pass_down is not implemented!')

    @abstractmethod
    def receive(self):
        raise Exception('receive is not implemented!')

    @abstractmethod
    def append_header(self, message):
        raise Exception('append_header is not implemented!')

    @abstractmethod
    def get_payload(self, message):
        raise Exception('get_payload is not implemented!')
