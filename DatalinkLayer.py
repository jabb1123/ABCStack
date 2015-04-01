from StackLayer import StackLayer
import threading

class DatalinkLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)

    def pass_down(self):
        pass

    def receive(self):
        message = self.below_queue.get()
        print('Datalink: ', message)
