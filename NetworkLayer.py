from StackLayer import StackLayer
import configparser

class NetworkLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)

        self.config = configparser.ConfigParser()
        self.config.read('addresses.ini')
        self.src_ip = self.config['DEFAULT']['ip'].replace("'", "")

    def pass_down(self, message):
        dest_ip = 'AR' # TODO: retrieve destination IP
        return self.src_ip + dest_ip + message

    def receive(self):
        message = self.below_queue.get()

        print('Source IP:', message[0:2])
        print('Dest IP:', message[2:4])

        self.above_queue.put(message[4:])
