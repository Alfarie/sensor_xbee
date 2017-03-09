
import threading
import time

class CheckConnection(threading.Thread):
	"""docstring for CheckConnection"""
	def __init__(self,socket):
		threading.Thread.__init__(self)
		self.fcm01 = False
		self.fcm02 = False
		self.socketio = socket.socketIO
		self.start()

	def run(self):
		while True:
			data = {'cm01' : self.fcm01 , 'cm02': self.fcm02}
			try:
				self.socketio.emit('CHECK_CONNECTION', data)
			except AttributeError:
				time.sleep(2)
				continue

			# print('check Connection ')
			
			# print(data)
			self.fcm01 = False
			self.fcm02 = False
			
			time.sleep(2)
		