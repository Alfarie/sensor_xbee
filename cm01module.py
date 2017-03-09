import serial
class Cm01Module():
	"""docstring for Cm01Module"""
	def __init__(self, socket ,get_sensor):
		self.socketio = socket.socketIO
		self.get_sensor = get_sensor
		self.socketio.on('CM01_REQ_SETTING' , self.cm01_req_setting)

	def cm01_req_setting(self ,data):
		# print(data)
		# {u'phth': 50, u'phfeed': 2, u'ecth': 0.8, u'dt': 50, u'ecfeed': 4}
		phth = data['phth']
		phfeed = data['phfeed']
		ecth = data['ecth']
		ecfeed = data['ecfeed']
		dt = data['dt']
		cm01str = "{"+str(phth)+","+str(phfeed)+"," +str(ecth) + "," + str(ecfeed) + "," + str(dt) +"}"
		#print (cm01str)
		try:
			self.get_sensor.ser.write(cm01str)
		except serial.serialutil.SerialException:
			print('[CM01] Serial Error')		