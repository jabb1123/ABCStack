from StackLayer import StackLayer

class NetworkLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)

    def pass_down(self, message):
        return message

    def receive(self):
        message = self.below_queue.get()

        print('Source IP:', message[0])
        print('Dest IP:', message[1])

        self.above_queue.put(message[2:])
