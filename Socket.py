from socketIO_client import SocketIO, LoggingNamespace
import serial
import json
import threading

class Socket(threading.Thread):
		def __init__(self, url):
			threading.Thread.__init__(self)
			self.url = url
			self.isConnect = False
			# self.socketIO = None
			self.socketIO = SocketIO(self.url, 3000, LoggingNamespace)
			self.start()
			
		def listen(self):
			self.socketIO.on("connect", self.on_connect)
			self.socketIO.on('disconnect', self.on_disconnect)
			self.socketIO.on('reconnect', self.on_reconnect)
		def run(self):
			print('[GROBOT] connecting http://localhost:3000');
			# self.socketIO = SocketIO(self.url, 3000, LoggingNamespace)
			self.listen()
			while True:
				self.socketIO.wait(seconds=1)
			

		def on_connect(self):
			self.isConnect = True
			print("[GROBOT] http://localhost:3000 CONNECTED ")
		def on_disconnect(self):
			self.isConnect = False
			print("[GROBOT] DISCONNECTED")
		def on_reconnect(self):
			print("[GROBOT] CONNECTED")


