from PhysicalLayer import PhysicalLayer
from DatalinkLayer import DatalinkLayer

class ABCStack(object):
    def __init__(self, classes):
        self.layers = []

        for index, layer_class in enumerate(classes):
            if index > 0:
                self.layers.append(layer_class(below_queue = self.layers[index-1].above_queue))
            else:
                self.layers.append(layer_class())

if __name__ == '__main__':
    abc = ABCStack([PhysicalLayer, DatalinkLayer])
