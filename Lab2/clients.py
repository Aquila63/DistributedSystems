import sys, socket, struct, random

class Client():

	def __init__(self, port, message):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
		self.port = port
		self.message = message
		#print "Client started"
		s.connect(("localhost", self.port))
		s.sendall(self.message)
		recv_data = s.recv(1000)
		#print self.ip
		print recv_data

#	def connect():
#		print "Client started"
#		s.connect(("127.0.0.1", self.port))
#		s.sendall(self.message);

if __name__ == '__main__':

	port = int(sys.argv[1])
	for i in range(100):
		Client(port, "HELO hello\n")
	Client(port, "KILL_SERVICE\n")
	
	