import RPi.GPIO as gpio
import smbus
import time
import picamera
import base64
import io
import urllib
import urllib2, json
import subprocess
import contextlib
import Queue
import threading

from datetime import datetime
from threading import Thread

# Software-related constants
URL = 'http://localhost:8000/dashboard/triggers/triggers/'
LOGIN_URL = 'http://localhost:8000/users/login/'
USERNAME = 'ivo'
WEB_PASSWORD = 'sexbog34'
TMP_IMAGE_FILENAME = 'image.jpg'

# Hardware-related constants
ARDUINO_ADDRESS = 0x04
bus = smbus.SMBus(1)
gpio.setmode(gpio.BOARD)

MATRIX_KEYS = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
]

MATRIX_ROW_PINS = [29, 31, 33, 35]
MATRIX_COL_PINS = [11, 13, 15]

PASSWORD = [1, 3, 3, 7]
SYSTEM_STATUS_LED_PIN = 40

system_online = False

def setup_matrix():
    for column_pin_index in range(3):
        gpio.setup(MATRIX_COL_PINS[column_pin_index], gpio.OUT)
        gpio.output(MATRIX_COL_PINS[column_pin_index], 1)

    for row_pin_index in range(4):
        gpio.setup(MATRIX_ROW_PINS[row_pin_index], gpio.IN, pull_up_down = gpio.PUD_UP)

def take_picture():
    camera = picamera.PiCamera()
    camera.capture(TMP_IMAGE_FILENAME, use_video_port=True)

def start_stream():
    p = subprocess.Popen(
            'sudo service uv4l_raspicam start',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()

def stop_stream():
    p = subprocess.Popen(
            'sudo service uv4l_raspicam stop',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()

def send_trigger_update(sensor_id):
    base64_encoded_img = base64.encodestring(
        open(TMP_IMAGE_FILENAME, "rb").read()
    )

    handler = urllib2.HTTPHandler()
    opener = urllib2.build_opener(handler)

    post_fields = {
        'time_triggered': str(datetime.now()),
        'sensor': sensor_id,
        'image': base64_encoded_img
    }

    base64string = base64.b64encode('%s:%s' % (USERNAME, WEB_PASSWORD))

    data = urllib.urlencode(post_fields)
    request = urllib2.Request(URL, data=data)
    request.add_header('Content-Type', 'application/json')
    request.add_header('Authorization', 'Basic %s' % base64string)

    try:
        connection = opener.open(request)
    except urllib2.HTTPError, e:
        connection = e

    if connection.code == 200:
        data = connection.read()
        print data

def record_intrusion_video():
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_recording(stream, format='h264', quality=20)
        camera.wait_recording(5)
        camera.stop_recording()

def on_sensor_state_changed(sensor_id):
    stop_stream()

    take_picture()
    send_trigger_update(sensor_id)
    record_intrusion_video()

    start_stream()

def read_sensor_states():
    sensor_states = bus.read_i2c_block_data(ARDUINO_ADDRESS, 0, 3)
    return sensor_states

def read_sensors():
    try:
        global system_online
        while system_online:
	    gpio.output(SYSTEM_STATUS_LED_PIN, gpio.LOW)
            time.sleep(1)
	    gpio.output(SYSTEM_STATUS_LED_PIN, gpio.HIGH)

            sensor_states = read_sensor_states()
            if sensor_states[0]:
                on_sensor_state_changed(2)
            if sensor_states[1]:
                on_sensor_state_changed(3)
            if sensor_states[2]:
                on_sensor_state_changed(15)

    except KeyboardInterrupt:
        gpio.cleanup()

def read_matrix():
    try:
        global system_online
        keys_pressed = []

        while True:
            for column_pin_index in range(3):
                gpio.output(MATRIX_COL_PINS[column_pin_index], 0)

                for row_pin_index in range(4):
                    if gpio.input(MATRIX_ROW_PINS[row_pin_index]) == 0:
                        current_key = MATRIX_KEYS[row_pin_index][column_pin_index]
                        print current_key

                        if current_key == '*':
                            keys_pressed = []
                        elif current_key == '#':
                            if PASSWORD == keys_pressed:
                                if not system_online:
                                    system_online = True
                                    print "Alarm system is now on."

                                    sensors_thread = Thread(target = read_sensors)
                                    sensors_thread.start()
                                else:
                                    system_online = False
                                    gpio.output(SYSTEM_STATUS_LED_PIN, gpio.LOW)

                                    print "Alarm system is now off."
                            keys_pressed = []
                        else:
                            keys_pressed.append(current_key)

                        # Prevent repeated printing if the button is held
                        while (gpio.input(MATRIX_ROW_PINS[row_pin_index]) == 0):
                            pass

                        time.sleep(0.6)
                gpio.output(MATRIX_COL_PINS[column_pin_index], 1)
    except KeyboardInterrupt:
        gpio.cleanup()

setup_matrix()
gpio.setup(SYSTEM_STATUS_LED_PIN, gpio.OUT)
gpio.output(SYSTEM_STATUS_LED_PIN, gpio.LOW)

matrix_thread = Thread(target = read_matrix)
matrix_thread.start()
matrix_thread.join()

sensors_thread.join()
