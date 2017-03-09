from Socket import Socket
from GetSensor import getSensor
from cm01module import Cm01Module


socket = Socket("http://localhost:3000")
get_sensor = getSensor(socket)
cm01module = Cm01Module(socket,get_sensor)