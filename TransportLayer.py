from StackLayer import StackLayer

class TransportLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)

    def pass_down(self, message):
        return message

    def receive(self):
        message = self.below_queue.get()

        print('Source Port:', message[0])
        print('Dest Port:', message[1])
        print('Message:', message[2:])
