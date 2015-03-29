from abc import ABCMeta, abstractmethod

class StackLayer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def pass_up ():
        raise Exception('pass_up is not implemented!')

    @abstractmethod
    def pass_down ():
        raise Exception('pass_down is not implemented!')
