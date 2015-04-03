import queue as q
import threading as t
from collections import OrderedDict
import user as u
import morrowsocket as s

class ChatServer(object):

    def __init__(self, ip=None, port=69):
            

        # Initilize variables
        self.serverlog = []
        self.users = {}
        self.buflen = 65500
        self.ip = ip
        self.port = port
        self.socket = None

        # Thread control booleans
        self.closing = False
        self.disp_output = True
        self.output_msgs = []

        # Server UI Setup
        self.available_cmds = OrderedDict([('.help', self.help),
                                           ('.showLog', self.showLog),
                                           ('.clearLog', self.clearLog),
                                           ('.close', self.close)])

        # Client UI Setup
        self.user_cmds = OrderedDict([('login', self.login)])

        # Start actual recieving thread
        server_thread = t.Thread(target=self.runServer)
        server_thread.start()

        # Allow user interrupts to issue commands
        self.runCLI()

    # ----- Private UI Methods ----- #
    def runCLI(self):
        while not self.closing:
            input("\n")  # Continue to cmd prompt when user hits the enter key
            self.disp_output = False  # Temporarily stop displaying server output
            print("\n")

            cmd = input('--> Enter Cmd: ')
            cmd = cmd.split()

            if len(cmd) > 0 and cmd[0] in self.available_cmds:
                if len(cmd) >= 1:
                    args = cmd[1:]
                else:
                    args = []

                self.available_cmds[cmd[0]].__call__(args)

            # Resume server output and displayed the held messages
            self.disp_output = True
            for item in self.output_msgs:
                print(item)
            self.output_msgs = []

    def showLog(self, *args):
        print("#----- Start of Server Log ----- #")
        print("Server log contains {} entries".format(len(self.serverlog)))
        if self.serverlog:
            for (counter, item) in enumerate(self.serverlog):
                print("Entry No. {}:  ".format(counter) + item)
        print("#----- End of Server Log-----#")

    def clearLog(self, *args):
        self.serverlog = []
        print("#----- Server Log Cleared -----#")

    def help(self, *args):
        """ Display a list of commands and available applications. """

        if self.available_cmds:
            dir_text = "Enter commands in the format 'cmd [args]'. Available commands: \n"
            for cmd in self.available_cmds.keys():
                dir_text += " -" + cmd + "\n"
        else:
            dir_text = "No commands available."

        print(dir_text + "\n")

    def close(self, *args):
        self.disp_output = False  # Catch any final messages and suppress them
        self.closing = True
        print("#----- Server Shutdown -----#")

    # ----- Private Message Methods ----- #
    def runServer(self):
        socket, AF_INET, SOCK_DGRAM, timeout = s.Socket, s.AF_INET, s.SOCK_DGRAM, s.timeout

        with socket(AF_INET, SOCK_DGRAM) as sock:

            # Socket setup
            self.socket = sock
            self.ip = sock.gethostbyname("Falafel")
            sock.bind((self.ip, self.port))
            sock.settimeout(1)

            print("Chat Server started on IP Address {} and port {}".format(self.ip, self.port))
            print("To enter a comand, first press the enter key, then enter the command at the displayed prompt.")

            # Main loop
            while not self.closing:
                try:
                    # Check socket & parse data
                    data = sock.recvfrom(self.buflen)
                    bytearray_msg, address = data
                    msg = bytearray_msg.decode("UTF-8")

                    # Message display & logging
                    msg_output = "\nMessage received from ip address {}, port {}:\n".format(address[0], address[1])
                    msg_output += msg + "\n"
                    self.serverlog.append(msg_output)

                    # Account for when input is being taken
                    if self.disp_output:
                        print(msg_output)
                    else:
                        self.output_msgs.append(msg_output)

                    # Add new users and relay messages
                    if msg:
                        if msg[0] == '.':
                            self.login(msg[7:], address)
                        else:
                            self.relayMessage(msg, address)
                            

                # Allows socket's recvfrom to timeout safely
                except q.Empty:
                    continue

    def sendMessage(self, msg, address):
        """ Sends a message to the destination IP """
        if isinstance(msg, list):
            msg = " ".join(msg)

        # Send Message
        self.socket.sendto(msg.encode("UTF-8"), address)

    def relayMessage(self, msg, address):
        """ Repeats a message from the given source IP, if valid. """
        if not (address in self.users):
            self.sendMessage("Please login with the '.login' command.", address)
            relay_msg = "Server did not relay message because user is not logged in."
        elif len(msg) >= self.buflen:
            self.sendMessage("Message was too long and has not been sent.", address)
            relay_msg = "Server did not relay message due to length."
        else:
            for adr in self.users:
                msg = self.users[address].alias + ": " + msg
                if not (adr == address):
                    self.sendMessage(msg, adr)
            relay_msg = 'Server relayed message: ' + msg + ' from ' + address
        print(relay_msg)
        self.serverlog.append(relay_msg)

    # ----- User Commands ----- #
    def login(self, alias, address):
        if not alias:
            self.sendMessage("Login failed. No alias submitted.", address)
            return

        if isinstance(alias, list):
            alias = alias[0]

        self.users[address] = u.User(alias, address)

        welcome = alias + " has joined the server."
        print(welcome)
        self.serverlog.append(welcome)
        
        for adr in self.users:
            self.sendMessage(welcome, adr)

if __name__ == "__main__":
    ChatServer()
