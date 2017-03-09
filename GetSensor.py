import threading
import time
import serial
import json
from CheckConnection import CheckConnection


class getSensor( threading.Thread):
	def __init__(self,socket):
		threading.Thread.__init__(self)
		# self.socketIO = socket.socketIO
		while(not self.getPort()):
			temp=True

		self.sensorData = {'temp': 0.0 , 'humi': 0.0 , 'co2': 0.0 , 'ph':0.0 , 'ec': 0.0 , 'wt': 0.0}
		self.socketio = socket.socketIO
		self.checkConnection = CheckConnection(socket)

		self.start()
	def run(self):
		st = False
		line =""
		while 1:
			try:
				ch = self.ser.read()
				
				if ch == "{" :
					st = True
				if st:
					line += ch
				if ch == "}":

					line = line.replace('{','')
					line = line.replace('}','')
					line = line.replace('\x00' , '')
					
					
					if line.startswith('cm02'):
						line = line.replace('cm02','')
						data = line.split(',')
						for i, x in enumerate(data):
							try:
								data[i] = float(x)
							except ValueError:
								line=""
								continue

						#set variable 
						self.sensorData['temp'] = data[0]
						self.sensorData['humi'] = data[1]
						self.sensorData['co2'] = data[2]
						self.checkConnection.fcm02 = True

					elif line.startswith('cm01'):
						line = line.replace('cm01','')
						data = line.split(',')
						for i, x in enumerate(data):
							try:
								data[i] = float(x)
							except ValueError:
								line=""
								continue

						self.sensorData['ph'] = data[0]
						self.sensorData['ec'] = data[1]
						self.sensorData['wt'] = data[2]
						self.checkConnection.fcm01 = True

					# print(self.sensorData)
					# self.socketio.emit('SENSOR_DATA' , self.sensorData)
					try:
						self.socketio.emit('SENSOR_DATA' , self.sensorData)
					except AttributeError:
						print("[GROBOT][ERROR] AttributeError")
						continue
					line=""

					st = False
			except serial.serialutil.SerialException:
				while(not self.getPort()):
					temp=True
	def getPort(self):
		port = '/dev/ttyUSB'
		t = False;
		for i in range(20):
			p = port+ str(i)
			try:
				self.ser = serial.Serial(p)
				print ('[GROBOT] port ' + p + ' connected')
				t= True
				break;
			except serial.serialutil.SerialException:
				# print('[GROBOT] Fail to connect port ' + p)
				time.sleep(0.1)
				continue
		if not t:
			print('Could not connect serial port')
		return t

	