from DatalinkLayer import DatalinkLayer

class RouterDatalinkLayer(DatalinkLayer):

     def receive(self):

        message = self.below_queue.get()

        if message[1] == " ":
            self.above_queue.put(message)
            print('Router Data Link Receive (Blank):', message)

        elif message[1] == 'R':
            dest_lan = message[5]
            dest_host = message[6]
            message = message[0] + self.iptable['DEFAULT'][dest_host] + message[2:]

            print('Router Data Link Receive (To R):', message)
            
            #passing down routed message with found mac address
            self.pass_down(message)

     def pass_down(self, message):
        #check to see if passing down for an informational message
        #if informational change mac information
        #if a simple redirect message then just pass it down
        
        if message[1] == " ":
            print('Source MAC:', message[0])
            print('Dest MAC:', message[1])
            print('IP Protocol:', message[2])
            #sending back the ip to the transmiting pi

            #getting src of router from config
            src_mac = self.src_mac
            dest_mac = message[0]
            ip_protocol = message[2]

            message = self.src_mac + dest_mac + message[2:]

        print('Router DataLink Pass Down:', message) 

        return message
            
            
        
