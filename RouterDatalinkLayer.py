from DatalinkLayer import DatalinkLayer

class RouterDatalinkLayer(DatalinkLayer):
     def receive(self):
        while(True):
            message = self.below_queue.get()

            if message[1] == " ":
                print('Source MAC:', message[0])
                print('Dest MAC:', message[1])
                print('IP Protocol:', message[2])
                #sending back the ip to the transmiting pi

                #getting src of router from config
                src_mac = self.src_mac
                dest_mac = message[0]
                ip_protocol = message[2]

                #creating new ip for newly connected pi
                lan = self.config['DEFAULT']['lan'].replace("'","")
                host = str(len(self.iptable['DEFAULT']))

                iptable_file = open('iptable.ini', 'w')
                self.iptable.set('DEFAULT', host, message[0])
                self.iptable.write(iptable_file)
                iptable_file.close()

                src_ip = lan + self.config['DEFAULT']['host'].replace("'","") 
                dest_ip = lan + host

                # TODO: Calculate checksum
                check_sum = 'CCCC'

                message = self.src_mac + dest_mac + src_ip + dest_ip + check_sum + message[11:]
                print('MESSAGE TO BE SENT: ', message)

                self.above_queue.put(message)

            elif message[1] == 'R':
                dest_lan = message[5]
                dest_host = message[6]
                message = message[0] + self.iptable['DEFAULT'][dest_host] + message[2:]

                print('Router Data Link Receive (To R):', message)
                
                #passing down routed message with found mac address
                self.above_queue.put(message)
                
        
