from abc import ABCMeta, abstractmethod

class StackLayer(object):
    __metaclass__ = ABCMeta

@abstractmethod
def pass_up ():
    pass

@abstractmethod
def pass_down ():
    pass
