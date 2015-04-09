from ABCStack import ABCStack
from PhysicalLayer import PhysicalLayer
from RouterDatalinkLayer import RouterDatalinkLayer
import configparser

class RouterABCStack(ABCStack):
    def __init__(self, classes):
        super().__init__(classes)

        iptable = configparser.ConfigParser()
        iptable.read('iptable.ini')
        config = configparser.ConfigParser()
        config.read('config.ini')

        iptable_file = open('iptable.ini', 'w')
        iptable.set('IPTABLE', '0', config['CONFIG']['mac'].replace("'", ""))
        iptable.write(iptable_file)
        iptable_file.close()

        message = self.layers[len(self.layers)-1].above_queue.get()
        print("STACK RECEIVED: " + message)
        #SENDING MESSAGE FROM DATALINKLAYER TO PHYSICAL
        self.pass_down(len(self.layers)-2, message)
