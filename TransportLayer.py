from StackLayer import StackLayer

class TransportLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)

    def pass_down(self, message):
        # TODO: retrive ports
        src_port = '1'
        dest_port = '2'
        return src_port + dest_port + message

    def receive(self):
        message = self.below_queue.get()

        print('Source Port:', message[0])
        print('Dest Port:', message[1])
        print('Message:', message[2:])
