import RPi.GPIO as GPIO
import time

class Module:

	def __init__(self, pin):
		self.__pin = pin
		GPIO.setup(pin, GPIO.OUT)
	
	def turn_on(self):
		GPIO.output(self.__pin, 1)
	
	def turn_off(self):
		GPIO.output(self.__pin, 0)
	
	def set_pin(self, pin):
		self.__pin = pin

	def get_pin(self, pin):
		return self.__pin

	def blink(self, timing):
		self.turn_on()
		time.sleep(timing)
		self.turn_off()
