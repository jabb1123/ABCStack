import ABCStack as stack
import atexit
import RPi.GPIO as GPIO
import time


if __name__ == '__main__':
    atexit.register(GPIO.cleanup)
    abc = stack.ABCStack([stack.PhysicalLayer, stack.DatalinkLayer, stack.NetworkTransportLayer])
    #TODO: CHECK TO SEE IF MISSING IP AND ROUTER INFORMATION
    #abc.prompt(informational=True)
    
    while True:
        abc.prompt()
    
