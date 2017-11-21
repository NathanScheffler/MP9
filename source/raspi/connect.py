import socket
from datetime import datetime

class Connection:
	def __init__(self, ip, port):
		self.__s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.__ip = ip
		self.__port = port
	
	def send(self, msg):
		try:
			self.__s.sendto(msg.encode('utf-8'), (self.__ip, self.__port))
		except Exception as e:
			print("Erreur lors de l'envoi" + str(e))
			return

	def send_detection(self, state):
		self.send(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ";" + str(state))

