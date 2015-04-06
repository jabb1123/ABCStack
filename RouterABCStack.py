from ABCStack import ABCStack
from PhysicalLayer import PhysicalLayer
from RouterDatalinkLayer import RouterDatalinkLayer

class RouterABCStack(ABCStack):
    def __init__(self, classes):
        super().__init__(classes)
        message = self.layers[len(self.layers)-1].above_queue.get()
        self.pass_down(len(self.layers)-1, message)
