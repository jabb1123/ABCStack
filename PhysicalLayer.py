from GPIO import *
from MorseTranslator import *
from datetime import datetime
import time
import threading
import math
from queue import Queue
from StackLayer import StackLayer

class PhysicalLayer(StackLayer):
    def __init__(self, receive_queue):
        StackLayer.__init__(self)

        self.input_pin = 23
        self.output_pin = 17
        self.receive_rate = 1/1000;
        self.transmit_rate = 1/100;

        prepare_pin(self.input_pin)

        self.reading = False

        self.previous_edge = time.time()
        self.current_edge = None

        self.pulse_list = []
        self.receive_queue = receive_queue

        #self.stack = MorseBJStack()

        # detect rising and falling edges
        GPIO.add_event_detect(self.input_pin, GPIO.BOTH, callback=self.edge_found)
        
    def edge_found(self, pin):
        # Callback for GPIO edge detect
        
        self.current_edge = time.time()
        time_passed = self.current_edge - self.previous_edge
        
        # duration and state of received pulse
        signal = 0 if GPIO.input(self.input_pin) else 1        
        pulse = (round(time_passed / self.transmit_rate), signal)
        print(pulse)

        self.previous_edge = self.current_edge

        # handle start sequence
        if (pulse[1] and pulse[0] > 15 and pulse[0] <= 20):
            # reset queue of pulses for new transmission
            self.pulse_list = []
            self.reading = True

        # handle stop sequence
        elif (pulse[1] and pulse[0] >= 30):
            self.receive_queue.put(self.pulse_list)
            self.translate()
            self.reading = False

        elif self.reading:
            # insert received pulse in queue
            self.pulse_list.append(pulse)

    def translate(self):
        # Translate pulses in queue to characters
        print('Receive Queue: ' + str(layer.receive_queue.get()))
        print('Translating.')

    def transmit(self, pulses=[(20,1), (1,0), (1,1), (1,0), (40,1)]):
        prepare_pin(self.output_pin, True)
        for pulse in pulses:
            if pulse[1]:
                turn_high(self.output_pin)
            else:
                turn_low(self.output_pin)
            delay(self.transmit_rate * pulse[0])
        turn_low(self.output_pin)
        delay(1) # for detecting the last pulse

    def pass_up(self):
        with Safeguards():
            self.receive()

    def pass_down(self):
        with Safeguards():
            self.transmit()

if __name__ == '__main__':
    receive_queue = Queue()
    layer = PhysicalLayer(receive_queue)
    
    delay(.01) # allowing edge detection thread to start
    layer.pass_down()
