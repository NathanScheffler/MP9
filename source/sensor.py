import RPi.GPIO as GPIO

class Sensor:

	def __init__(self, pin):
		GPIO.setup(pin, GPIO.IN)
		self.__pin = pin

	def set_pin(self, pin):
		self.__pin = pin

	def get_etat(self):
		return GPIO.input(self.__pin)

	
