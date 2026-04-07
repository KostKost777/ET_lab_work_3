import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
phototranz = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(phototranz, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(phototranz))
    time.sleep(0.05)