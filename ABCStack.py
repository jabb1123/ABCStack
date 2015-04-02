from PhysicalLayer import PhysicalLayer
from DatalinkLayer import DatalinkLayer
from NetworkLayer import NetworkLayer
from TransportLayer import TransportLayer

class ABCStack(object):
    def __init__(self, classes):
        self.layers = []
        for index, layer_class in enumerate(classes):
            if index > 0:
                self.layers.append(layer_class(below_queue=self.layers[index-1].above_queue))
            else:
                self.layers.append(layer_class(below_queue=None))

        self.pass_down(len(self.layers)-1, 'HI')

    def pass_down(self, i, message):
        if i < 0:
            return
        return self.pass_down(i-1, self.layers[i].pass_down(message))

if __name__ == '__main__':
    abc = ABCStack([PhysicalLayer, DatalinkLayer, NetworkLayer, TransportLayer])
