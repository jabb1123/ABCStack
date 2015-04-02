from StackLayer import StackLayer
import configparser

class DatalinkLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)

        # retrive mac address  
        self.config = configparser.ConfigParser()
        self.config.read('addresses.ini')
        self.src_mac = self.config['DEFAULT']['mac'].replace("'", "")

    def pass_down(self, message):
        dest_mac = self.config['IPTABLE'][message[2:4]].replace("'", "")
        # TODO: retrieve destination IP protocol
        ip_protocol = 'A'
        return self.src_mac + dest_mac + ip_protocol + message

    def receive(self):
        message = self.below_queue.get()
        if message:            
            if message[1] == self.src_mac:
                print('Source MAC:', message[0])
                print('Dest MAC:', message[1])
                print('IP Protocol:', message[2])

                self.above_queue.put(message[3:])
            else:
                print('Routed to', message[1])

        else:
            print('Requesting IP Address...')
            # TODO: Grant IP Address - HOW TO ACCESS 'A'?
            self.config['IPTABLE'][self.src_mac] = self.config['DEFAULT']['ip'].replace("'","")[0] + self.src_mac
            print ('IP Address:', self.config['IPTABLE'][self.src_mac])
            
