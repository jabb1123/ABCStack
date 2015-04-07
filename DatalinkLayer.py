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
        if message[1] == self.src_mac:
            ip_protocol = message[2]
            dest_mac = message[1]
            src_mac = message[0]

            #CHECKS TO SEE IF INFORMATIONAL PROTOCOL
            if ip_protocol == "C":
                #STORE ROUTER MAC ADDRESS
                config_file = open('config.ini', 'w')
                self.config.set('DEFAULT', 'router', dest_mac)
                self.config.write(config_file)
                config.close()
            else:
                print('Source MAC:', message[0])
                print('Dest MAC:', message[1])
                print('IP Protocol:', message[2])

                #TODO: STORE REFERENCE OF MESSAGE SENDER INTO CACHING MECHANISM
                self.temp_store(src_mac)

                self.above_queue.put(self.get_payload(message))
        else:
            print('Routed to', message[1])

    def append_header(self, message):
        try:
            #CHECK CACHE FOR MESSAGE
            #TODO: THIS IS BROKEN, HAVE TO ITERATE THROUGH VALUES BECAUSE IP STORES HOST AS KEY
            dest_mac = self.iptable['DEFAULT'][message[2:4]].replace("'", "")
        except:
            #SEND MESSAGE TO ROUTER
            """
            TODO: CHECK TO SEE IF ROUTER EXISTS
                      IF ROUTER DOES NOT EXIST,
                      MAKE IP_PROTOCOL = 'C',
                      SET DEST_MAC = ' ' in order to
                      indicate informational packet.
            """
            dest_mac = self.config['DEFAULT']['router'].replace("'", "")

        ip_protocol = 'A'

        return self.src_mac + dest_mac + ip_protocol + message

    def get_payload(self, message):
        return message[3:]

    def temp_store(self, mac):
        import json
        pair = {mac: None}
        with open('temp.txt', 'w') as tempfile:
            json.dump(pair, tempfile,indent=4)
