from StackLayer import StackLayer
import threading
import configparser

class DatalinkLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)
        self.config = configparser.ConfigParser()

    def pass_down(self, message):

        self.config.read('addresses.ini')
        # retrive mac address and remove quotation marks      
        src_mac = self.config['DEFAULT']['mac'].replace("'", "")
        src_lan = 'A'
        # src_host = # get source host from router

        if message[0] == src_mac:
            print('My Message.')
            return message
        else:
            print('Re-Route Message.')
            return

    def receive(self):
        message = self.below_queue.get()
        src_mac = message[0]
        dest_mac = message[1]
        print('Source:', src_mac)
        print('Dest:', dest_mac)
        print('Message:', message[2:])

        if dest_mac == 'R': # router packet
            print('Router Packet')
        else: # client packet
            print('Route to', dest_mac)
            
