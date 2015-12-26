import sys, socket, struct, random, re

class Client():

	def create_join_message(self, name, handle):
               message = "JOIN_CHATROOM: {0}\nCLIENT_IP: {1}\nPORT: {2}\nCLIENT_NAME: {3}".format(name, 0, 0, handle)
               return message
	
	def create_leave_message(self, name, jid, handle):
		message = "LEAVE_CHATROOM: {0}\nJOIN_ID: {1}\nCLIENT_NAME: {2}".format(name, jid, handle)
		return message  
		
	def create_chat_message(self, name, jid, handle, message):
		message = "CHAT: {0}\nJOIN_ID: {1}\nCLIENT_NAME: {2}\nMESSAGE: {3}".format(name, jid, handle, message)
		return message
		
	def __init__(self, port):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(5)
		self.ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
		self.port = port
		#Regex to extract the join id returnd by the server
		r = re.compile("JOIN_ID: (.*?)$", re.MULTILINE)
		message = self.create_join_message("room1", "jdoe")
		#print "Client started"
		s.connect(("0.0.0.0", self.port))
		s.sendall(message)
		recv_data = s.recv(1000)
		res = r.search(recv_data)
		self.join_id = res.group(1)
		print recv_data
		
		print "\nSending Chat Message"
		message = self.create_chat_message("room1", self.join_id, "jdoe", "Hello\n\n")
		s.sendall(message)
		recv_data = s.recv(1000)
		print recv_data

		print "\nLeaving"
		message = self.create_leave_message("room1", self.join_id, "jdoe")
		s.sendall(message)
		recv_data = s.recv(1000)
		print recv_data

		"""while(1):
			try:
				recv_data = s.recv(1000)
				if(self.join_id == None):
					res = r.search(recv_data)
					self.join_id = res.group(1)
				print recv_data
			except socket.timeout:
				continue"""

#	def connect():
#		print "Client started"
#		s.connect(("127.0.0.1", self.port))
#		s.sendall(self.message);

if __name__ == '__main__':

	port = int(sys.argv[1])
	Client(port)
	
	
