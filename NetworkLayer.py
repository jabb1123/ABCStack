from StackLayer import StackLayer
import configparser

class NetworkLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)

        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.src_ip = self.config['DEFAULT']['lan'].replace("'", "") + self.config['DEFAULT']['host'].replace("'","")
    
    def pass_down(self, message):
        return self.append_header(message)

    def receive(self):
        message = self.below_queue.get()

        print('Source IP:', message[0:2])
        print('Dest IP:', message[2:4])
        print('Check Sum:', message[4:8])

        self.above_queue.put(self.get_payload(message))

    def append_header(self, message):
        dest_ip = 'A0' # TODO: retrieve destination IP from MorseSockets Server
        check_sum = 'CCCC' # TODO: implement check sum
        return self.src_ip + dest_ip + check_sum + message

    def get_payload(self, message):
        return message[8:]
