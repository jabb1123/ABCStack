from StackLayer import StackLayer
import configparser

class NetworkTransportLayer(StackLayer):
    def __init__(self, below_queue):
        super().__init__(below_queue)

        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.iptable = configparser.ConfigParser()
        self.iptable.read('iptable.ini')
        self.src_ip = self.config['DEFAULT']['lan'].replace("'", "") + self.config['DEFAULT']['host'].replace("'","")

    def pass_down(self, message):
        return self.append_header(message)

    def receive(self):
        message = self.below_queue.get()

        src_lan = message[0:1]
        src_host = message[1:2]

        dest_lan = message[2:3]
        dest_host = message[3:4]

        #CHECK TO SEE IF THE PACKET IS PURELY INFORMATIONAL
        if src_host == " ":
            #STORE INFORMATION
            config_file = open('config.ini', 'w')
            self.config.set('DEFAULT', 'lan', dest_lan)
            self.config.set('DEFAULT', 'host', dest_host)
            self.config.write(config_file)
            config.close()
        else:
            print('Source IP:', message[0:2])
            print('Dest IP:', message[2:4])
            print('Check Sum:', message[4:8])
            self.create_ip_cache(create_ip_cache)

            self.above_queue.put(self.get_payload(message))

    def append_header(self, message):
        dest_ip = 'A0' # TODO: retrieve destination IP from MorseSockets Server
        check_sum = 'CCCC' # TODO: implement check sum
        return src_port + dest_port + self.src_ip + dest_ip + check_sum + message

    def get_payload(self, message):
        return message[8:]

    def create_ip_cache(self, host):
        import json
        with open('temp.txt', 'r+') as tempfile:
            temp = json.load(tempfile)
            temp_mac = temp.keys()[0]

            #ADD MESSAGE TO CACHE
            iptable_file = open('iptable.ini', 'a')
            self.iptable.set('DEFAULT', host, temp_mac)
            self.iptable.write(iptable_file)
            iptable_file.close()

            tempfile.truncate()
