from NetworkLayer import NetworkLayer

class RouterNetworkLayer(NetworkLayer):
    
    def receive(self):

        message=self.below_queue.get()

        #creating new ip for newly connected pi
        lan = self.config['DEFAULT']['lan'].replace("'","")
        host = str(len(self.iptable['DEFAULT']))

        self.iptable['DEFAULT'][host] = src_mac

        src_ip = lan + self.config['DEFAULT']["host"].replace("'","") 
        dest_ip = lan + host

        # TODO: Calculate checksum
        check_sum = 'CCCC'

        message = message[0:3] + src_ip + dest_ip + check_sum + " "
        self.pass_down(message)

        print('Router Network Receive:', message) 

    def pass_down(self, message):
        print('Router Network Pass Down:', message) 
        return message
