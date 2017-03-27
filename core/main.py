import time
import RPi.GPIO as io

from urllib.parse import urlencode
from urllib.request import Request, urlopen

io.setmode(io.BCM)

contact_pin = 7
vibration_pin = 11
sound_pin = 13

pins_array = [contact_pin, vibration_pin, sound_pin]

url = 'http://localhost:8000/triggers'

def setup_door():
    # So, that input pin uses the extra argument (pull_up_down=io.PUD_UP).
    # This activates an internal resistor that makes the input HIGH
    # (pulled-up) unless something stronger (like a switch connecting it
    # to GND) pulls it LOW.

    io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)

def setup_vibration():
    io.setup(vib_pin, io.IN)

def setup_sound():
    io.setup(sound_pin, io.IN)

def main():
    setup_door()
    setup_vibration()
    setup_sound()

    while True:
        for pin in pins_array:
            if io.input(i):
                sensor_id = pins_array.index(contact_pin) + 1
        time.sleep(0.5)

def trigger_sensor(sensor_args):
    request = Request(url, urlencode(sensor_args).encode())

main()
