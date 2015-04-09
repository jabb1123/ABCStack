import RouterABCStack as stack
import configparser
import atexit
import RPi.GPIO as GPIO
import time

if __name__ == '__main__':
    atexit.register(GPIO.cleanup)
    abc = stack.RouterABCStack([stack.PhysicalLayer, stack.RouterDatalinkLayer])
    while True:
        time.sleep(1000000)
