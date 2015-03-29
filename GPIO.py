import time
import RPi.GPIO as GPIO

class Safeguards:
    def __enter__(self):
        return self
    def __exit__(self,*rabc):
        GPIO.cleanup()
        print("Safe exit succeeded")
        return not any(rabc)

def prepare_pin(pin=23, out=False):
    GPIO.setmode(GPIO.BCM)  #use Broadcom (BCM) GPIO numbers on breakout pcb
    
    if out:
        GPIO.setup(pin, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    else:
        GPIO.setup(pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # allow pi to read levels

def read_pin(pin):
    return GPIO.input(pin)  # set 3.3V level on GPIO output

def delay(duration):            # sleep for duration seconds where duration is a float.
    time.sleep(duration)

def turn_high(pin=17):
    GPIO.output(pin,GPIO.HIGH)  # set 3.3V level on GPIO output

def turn_low(pin=17):
    GPIO.output(pin,GPIO.LOW)   # set ground (0) level on GPIO output
