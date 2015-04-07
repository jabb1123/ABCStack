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


sock = MorseSocket(1,2)
