from GPIO import *
from MorseTranslator import *
from datetime import datetime
from time import sleep
import threading
import math
from queue import Queue

class PhysicalLayer(StackLayer):
    def __init__(self):
        StackLayer.__init__(self)

        self.input_pin = 23
        self.output_pin = 17
        self.receive_rate = 1/1000;
        self.transmit_rate = 1/100;

        self.reading = False
        self.gpio_state = GPIO.input(input_pin)
        self.previous_edge = datatime.now()
        self.current_edge = None

        self.pulse_queue = Queue()

        self.stack = MorseBJStack()

        # detect rising and falling edges
        GPIO.add_event_detect(self.input_pin, GPIO.BOTH, callback=self.edge_found)
        
    def edge_found(self, pin):
        # Callback for GPIO edge detect

        self.current_edge = datetime.now()
        time_passed = self.current_edge - self.previous_edge

        # duration and state of received pulse
        pulse = (math.ceil(time_passed/self.transmit_rate), self.gpio_state)

        self.previous_edge = self.current_edge
        self.gpio_state = GPIO.input(self.input_pin)

        # handle start sequence
        if (pulse[1] and pulse[0] > 10 and pulse[0] <= 20):
            # reset queue of pulses for new transmission
            self.pulse_queue = Queue()
            self.reading = True

        # handle stop sequence
        elif (pulse[1] and pulse[0] >= 30):
            self.translate()
            self.reading = False

        if self.reading:
            # insert received pulse in queue
            self.pulse_queue.put(pulse)

    def translate():
        # Translate pulses in queue to characters
        pass

    def receive():
        prepare_pin(self.input_pin)

    def transmit():
        prepare_pin(self.output_pin)
    
    def pass_up():
        with Safeguards():
            thread = threading.Thread(target=self.receive)
            thread.start()

    def pass_down():
        with Safeguards():
            pass
