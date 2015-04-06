import ABCStack as stack

if __name__ == '__main__':
    abc = stack.ABCStack([stack.PhysicalLayer, stack.DatalinkLayer, stack.NetworkLayer, stack.TransportLayer])
    abc.prompt()
