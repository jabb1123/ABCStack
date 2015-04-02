from StackLayer import StackLayer

class TransportLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)

    def pass_down(self, message):
        # TODO: retrieve ports from MorseSockets
        src_port = '01'
        dest_port = '02'
        return src_port + dest_port + message

    def receive(self):
        message = self.below_queue.get()

        print('Source Port:', message[0:2])
        print('Dest Port:', message[2:4])
        print('Message:', message[4:])
