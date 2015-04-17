import ABCStack as stack
import atexit
import RPi.GPIO as GPIO
import time
import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    config_file = open('config.ini', 'w')
    
    atexit.register(GPIO.cleanup)
    abc = stack.ABCStack([stack.PhysicalLayer, stack.DatalinkLayer, stack.SocketServerLayer])


    router = config['CONFIG']['router'].replace("'", "")
    print('Router:', router)
    if router == ' ':
        print('Sending Informational Packet...')
        abc.prompt(informational=True)

    while True:
        abc.prompt()
