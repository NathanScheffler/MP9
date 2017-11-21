from module import *

class Alarm(Module):
	def __init__(self, pinLed, pinBuz):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		self.led = Module(pinLed)
		self.buzzer = Module(pinBuz)

	def turn_on(self):
		self.led.turn_on()
		self.buzzer.turn_on()

	def turn_off(self):
		self.led.turn_off()
		self.buzzer.turn_off()

	def set_pin_led(self, pinLed):
		self.led = Module(pinLed, self.buzzer.get_pin)

	def set_pin_buzzer(self, pinBuz):
		self.buzzer = Module(self.led.get_pin, pinBuz)

