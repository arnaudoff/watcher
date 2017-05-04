import time
import RPi.GPIO as io
io.setmode(io.BOARD)

door_pin = 16

io.setup(door_pin, io.IN)  # activate input with PullUp

try:
    while True:
        if not io.input(door_pin):
            print("DOOR ALARM!")
        time.sleep(1)
except KeyboardInterrupt:
	io.cleanup()

