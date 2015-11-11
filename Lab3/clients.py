import sys, socket, struct, random

class Client():

	def create_join_message(self, name, handle):
               message = "JOIN_CHATROOM: {0}\nCLIENT_IP: {1}\nPORT: {2}\nCLIENT_NAME: {3}".format(name, 0, 0, handle)
               return message


	def __init__(self, port):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1.5)
		self.ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
		self.port = port
		message = self.create_join_message("room1", "jdoe")
		#print "Client started"
		s.connect(("0.0.0.0", self.port))
		s.sendall(message)
		while(1):
			try:
				recv_data = s.recv(1000)
				print recv_data
			except socket.timeout:
				continue

#	def connect():
#		print "Client started"
#		s.connect(("127.0.0.1", self.port))
#		s.sendall(self.message);

if __name__ == '__main__':

	port = int(sys.argv[1])
	Client(port)
	
	
