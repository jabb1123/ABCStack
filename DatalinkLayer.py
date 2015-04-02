from StackLayer import StackLayer
import threading
import configparser

class DatalinkLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)

        # retrive mac address  
        self.config = configparser.ConfigParser()
        self.config.read('addresses.ini')
        self.src_mac = self.config['DEFAULT']['mac'].replace("'", "")

    def pass_down(self, message):
        return message

    def receive(self):
        message = self.below_queue.get()

        if message[1] == self.src_mac:
            print('Source MAC:', message[0])
            print('Dest MAC:', message[1])
            print('IP Protocol:', message[2])
            print('Message:', message[3:])
        else:
            print('Routed to', message[1])
