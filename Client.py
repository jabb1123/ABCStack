import ABCStack as stack

if __name__ == '__main__':
    abc = stack.ABCStack([stack.PhysicalLayer, stack.DatalinkLayer, stack.NetworkLayer, stack.TransportLayer])
    #TODO: CHECK TO SEE IF MISSING IP AND ROUTER INFORMATION
    #abc.prompt(informational=True)
    abc.prompt()
