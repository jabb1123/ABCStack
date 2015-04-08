from StackLayer import StackLayer

import socketsbase as base
import json
import queue


AF_INET = base.AF_INET
SOCK_DGRAM = base.SOCK_DGRAM

# Internal Constants
_MORSOCK_SERVER_ADDR = ('localhost', 5280)  # Default address of the morstack server
_PORT_CAP = 100  # Number of morse ports to make available

class socket(base.socketbase):
    def __init__ (self, network_protocol=AF_INET, transport_protocol=SOCK_DGRAM):
        self.msg_queue = Queue()
        self.cmd_map = {
        "message" : "message function",
        "exception" : "exception function"
        }
        super().__init__(network_protocol, transport_protocol)

        self.socket = base.CN_Socket.socket(AF_INET, SOCK_DGRAM)

    def bind (self, ip, port=80):
        #send bind command

    def recvfrom (self, bufsize):
        #send bind command

    def sendto (self, message, address):
         #send bind command

    def message():
        pass

    def _send_command(self, command, params={}):
        serialized_command = serialize(command, params)
        self.socket.sendto(serialized_command, _MORSOCK_SERVER_ADDR)

    def _queue_message(self, msg, address):
        message_packet = (msg, address)
        self.msg_queue.put(message_packet)

    def serialize(command, params={}):
        return json.dumps(
            {
            "command" : command
            "params" : params
            }
        ).encode('utf-8')

    def deserialize(serialized):
        return json.loads(serialized)


class SocketServerLayer (StackLayer):
    
    def __init__(self, addr=_MORSOCK_SERVER_ADDR, verbose=False):
        self.verbose = verbose
        self.port_map = {}
        self.port_counter = 0
        self.CMD_MAP = {
            "sendto" : self.passDown,
            "bind" : self.bind,
            "register" : self.register,
            "close" : self.close
        }
        
        with sb.CN_Socket(2, 2) as self.sock:
            self.sock.bind(addr)          
            while True:
                data, addr = self.sock.recvfrom(8192)
                cmd_obj = deserialize(data)
                cmd_obj['params']['addr'] = addr
                self.CMD_MAP[cmd_obj['instruction']](**cmd_obj['params'])
                if self.verbose: print("Received the command {} from {}".format(data, addr))
                
        self.sock.close()

    def passUp(self, msg):
        """
        Grab IP/Port data and forward through internal socket to the
        related process in the port_map.
        """
        pass
           
    def pass_down(self, message):
        return self.append_header(message)

    def append_header(self, message):
        # TODO: retrieve ports from MorseSockets
        src_port = '01'
        dest_port = '02'

        return src_port + dest_port + message
    
    def bind(self, request_addr, addr):
        """
        Binds a process to the requested (ip, port) address if that combination
        is not already in use by another process. Returns a serialized exception
        to the requesting morstackclient if the address is not available
        """
        
        if request_addr in self.port_map.itervalues():
            exception = "Port in use"
        elif request_addr[1] > _PORT_CAP:
            exception = "Port number out of range. Ports numbers must be >0 and <{}".format(_PORT_CAP)
        else:
            del self.port_map[addr[1]]  # Clear old port reservation
            self.port_map[addr[1]] = request_addr[1]  # Reserve new port
            if self.verbose: print("Process on OS port {} bound to morse port {}".format(addr[1], request_addr[1]))
            return
        
        self.sendException(exception, addr)
            
    
    def register(self, addr):
        """
        Assign a morse port to a process when it starts up. The ports
        are assigned from 0 to _PORT_CAP and will find an available port
        if available. If a port is not available, it will return a serialized
        exception to the morstackclient.
        """
        
        for i in range(self.port_counter, self.port_counter + _PORT_CAP):
            port = i % _PORT_CAP
            
            # If an available port if found, adjust the port_counter for
            # future searches, and register the process to the port
            if port not in self.port_map:
                self.port_counter = port + 1
                self.port_map[addr[1]] = port
                if self.verbose: print("New process registered on OS port {} bound to morse port {}".format(addr[1], port))
                return
        
        # If no ports are available, forward an exception to the requesting client
        self.sendException("No ports available", addr)
        
    def close(self, addr):
        del self.port_map[addr[1]]  # Close port reservation
    
    def sendException(self, desc, addr):
        self.sock.sendto(serialize("exception", {"desc": desc}), addr)
        
def serialize(instruction, parameters={}):
    return json.dumps(
        {"instruction": instruction,
         "params": parameters
        }).encode('utf-8')

def deserialize(serialized):
    return json.loads(serialized.decode('utf-8'))
    
def forcedecode (encoded):
    try:
        return encoded.decode('utf-8')
    except TypeError:
        return encoded
    
    
# ----- TESTING CODE ----- #
if __name__ == "__main__":
    # sock = MorseSocket(1,2)
    print("-- Testing: ")
    with socket(AF_INET, SOCK_DGRAM) as test_sock:
        pass




