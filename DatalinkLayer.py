from StackLayer import StackLayer

class DatalinkLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)

    def pass_down(self):
        pass

