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

from datetime import datetime
from threading import Thread

URL = 'http://localhost:8000/dashboard/triggers/triggers/'
LOGIN_URL = 'http://localhost:8000/users/login/'
USERNAME = 'ivo'
PASSWORD = 'sexbog34'
TMP_IMAGE_FILENAME = 'image.jpg'
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

    cookies = urllib2.HTTPCookieProcessor()
    opener = urllib2.build_opener(cookies)
    urllib2.install_opener(opener)

    opener.open(LOGIN_URL)

    try:
        token = [x.value for x in cookies.cookiejar if x.name == 'csrftoken'][0]
    except IndexError:
        return False, "no csrftoken"

    params = dict(username=USERNAME, password=PASSWORD, \
        this_is_the_login_form=True,
        csrfmiddlewaretoken=token,
         )
    encoded_params = urllib.urlencode(params)

    with contextlib.closing(opener.open(LOGIN_URL, encoded_params)) as f:

        post_fields = {
            'time_triggered': str(datetime.now()),
            'sensor_id': sensor_id,
            'image': base64_encoded_img
        }

        req = urllib2.Request(URL)
        req.add_header('Content-Type', 'application/json')
        data = json.dumps(post_fields)

        response = urllib2.urlopen(req, data)
        print response

def record_intrusion_video():
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_recording(stream, format='h264', quality=20)
        camera.wait_recording(5)
        camera.stop_recording()

def on_sensor_state_changed(sensor_id):
    stop_stream()
    time.sleep(1)

    take_picture()
    send_trigger_update(sensor_id)
    record_intrusion_video()

    start_stream()

def read_sensor_states():
    sensor_states = bus.read_i2c_block_data(ARDUINO_ADDRESS, 0, 2)
    return sensor_states

def read_sensors():
    try:
        while True:
            time.sleep(1)
            sensor_result = read_sensor_states()
            if sensor_result[0] == 1:
                on_sensor_state_changed(2)
            if sensor_result[1] == 1:
                on_sensor_state_changed(3)
    except KeyboardInterrupt:
        gpio.cleanup()
    
def read_matrix():
    try:
        while True:
            for column_pin_index in range(3):
                gpio.output(MATRIX_COL_PINS[column_pin_index], 0)

                for row_pin_index in range(4):
                    if gpio.input(MATRIX_ROW_PINS[row_pin_index]) == 0:
                        print MATRIX_KEYS[row_pin_index][column_pin_index]

                        # Prevent repeated printing if the button is held
                        while (gpio.input(MATRIX_ROW_PINS[row_pin_index]) == 0):
                            pass

                        time.sleep(0.6)
                gpio.output(MATRIX_COL_PINS[column_pin_index], 1)
    except KeyboardInterrupt:
        gpio.cleanup()

setup_matrix()

sensors_thread = Thread(target = read_sensors)
sensors_thread.start()

matrix_thread = Thread(target = read_matrix)
matrix_thread.start()

sensors_thread.join()
matrix_thread.join()
