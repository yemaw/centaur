from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import LightSensor
import time 
import atexit
import random
import signal


red   = PWMLED(17)
green = PWMLED(27)
blue  = PWMLED(22)
light_sensor = LightSensor(18)


'''while True:
	light_sensor.wait_for_light()
	print("It's light! :)")
	light_sensor.wait_for_dark()
	print("It's dark :(")'''

'''while True:
	green.value = round(random.uniform(0, 0.8), 2)
	blue.value = round(random.uniform(0, 0.5), 2)
	red.value = round(random.uniform(0, 1), 2)
	time.sleep(round(random.uniform(0.01, 0.1), 2))'''
	
	
'''green.value = round(random.uniform(0, 0.8), 2)
	blue.value = round(random.uniform(0, 0.5), 2)
	red.value = round(random.uniform(0, 1), 2)
	time.sleep(round(random.uniform(0.01, 0.1), 2))'''
	
def lights_on():
	green.value = 1
	blue.value = 1 
	red.value = 1
	
def lights_off():
	green.value = 0
	blue.value = 0
	red.value = 0	
	•••••
	
light_sensor.when_dark = lights_on
light_sensor.when_light = lights_off

signal.pause()


'''
@atexit.register
def ledoff():
	red.value = 0
	green.value = 0
	blue.value = 0
'''
