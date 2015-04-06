from StackLayer import StackLayer
import configparser

class DatalinkLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)

        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.iptable = configparser.ConfigParser()
        self.iptable.read('iptable.ini')
        
        self.src_mac = self.config['DEFAULT']['mac'].replace("'", "")

    def pass_down(self, message):
        return self.append_header(message)

    def receive(self):
        message = self.below_queue.get()
        if message[0] == self.src_mac:
            print('Source MAC:', message[0])
            print('Dest MAC:', message[1])
            print('IP Protocol:', message[2])
            self.above_queue.put(self.get_payload(message))

        else:
            print('Routed to', message[1])

    def append_header(self, message):
        try:
            dest_mac = self.iptable['DEFAULT'][message[2:4]].replace("'", "")
        except:
            dest_mac = self.config['DEFAULT']['router'].replace("'", "")
        ip_protocol = 'A' # TODO: retrive IP Protocol from header

        return self.src_mac + dest_mac + ip_protocol + message

    def get_payload(self, message):
        return message[3:]
