import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button = 13
led = 26

GPIO.setup(button, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

state = 0
flag = False

while True:
    cur_state = GPIO.input(button)
    
    if cur_state and not flag:
        state = not state
        GPIO.output(led, state)
        flag = True
    
    elif not cur_state and flag:
        flag = False
    
    time.sleep(0.02)