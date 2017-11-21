#!/usr/bin/python3

from alarm import *
from sensor import *
from connect import *

SENPIN = 11
LEDPIN = 3
BUZPIN = 5

SERVER_IP = '10.16.2.150'
SERVER_PORT = 5000

def main():
	try:
		print("""
___  ___               _        ___  ___        _    _               
|  \/  |              (_)       |  \/  |       | |  (_)              
| .  . |  __ _   __ _  _   ___  | .  . |  ___  | |_  _   ___   _ __  
| |\/| | / _` | / _` || | / __| | |\/| | / _ \ | __|| | / _ \ | '_ \ 
| |  | || (_| || (_| || || (__  | |  | || (_) || |_ | || (_) || | | |
\_|  |_/ \__,_| \__, ||_| \___| \_|  |_/ \___/  \__||_| \___/ |_| |_|
                 __/ |                                               
                |___/                                                
		""")
		alarm = Alarm(LEDPIN, BUZPIN)
		sensor = Sensor(SENPIN)
		connection = Connection(SERVER_IP, SERVER_PORT)

		print("Detection active")

		while True:

			detect = sensor.get_etat()		
	
			if detect == 0:

				alarm.turn_off()
				time.sleep(0.1)

			elif detect == 1:

				print("Debut mouvement : " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
				connection.send_detection(1)

				while detect == 1:

					detect = sensor.get_etat()
					alarm.blink(0.5)
					time.sleep(0.5)

				print("Fin mouvement : " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
				connection.send_detection(0)

	except KeyboardInterrupt:
		print("\nInterrompu")
		alarm.turn_off()

if __name__ == '__main__':
	main()
