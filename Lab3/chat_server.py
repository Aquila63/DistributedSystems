import sys, SocketServer, threading, os, uuid, re
import Queue

class Chatroom():

	errors = {1: "Cannot connect to room"}
	client_list = []

	def __init__(self, name):
		self.name = name
		self.room_id = uuid.uuid4().int>>64

	def join_room(self, client, name):
		self.client_list.append(client)
		return uuid.uuid4().int>>64 #Return a unique join id
	

class ThreadPoolMixIn(SocketServer.ThreadingMixIn):

	pool_size = 10 #No. of threads in the pool
	student_id = "07988616e4e32911bc9f6a7571184b611fc93406d027a5c828a87664735ed383"
	chatrooms = {}

	def setup_rooms(self):
		self.r1 = Chatroom("room1")
		self.chatrooms["room1"] = self.r1
		self.r2 = Chatroom("room2")
		self.chatrooms["room2"] = self.r2

	#Main server loop
	def serve_forever(self):
		#Create the request queue
		self.request_queue = Queue.Queue(self.pool_size)
		self.setup_rooms()
		for t in range(self.pool_size):
			t = threading.Thread(target = self.process_request_thread) #Initialize threads
			#print "Starting pool thread ", t.name
			t.start()

		while 1:
			self.handle_request() #Get the ball rolling

	#Start handling the requests sent to the server
	def handle_request(self):
		#requests are esentially socket objects
		request, client_address = self.get_request()
		#Place in the queue
		self.request_queue.put((request,client_address))

	#Get a request from the queue
	def process_request_thread(self):
		while 1:
			#ThreadingMixIn.process_request_thread(self, self.request_queue.get())
			try:
				request, client_address = self.request_queue.get()
			except Queue.Empty:
				pass
			#Fufill request	
			self.finish_request(request, client_address)

	#This is where the work is done
	def finish_request(self, request, client_address):
		#Recieve data from client
		data = request.recv(1024)
		print data
		if data.startswith("JOIN_CHATROOM"):
			r = re.compile("JOIN_CHATROOM: (.*?)$", re.MULTILINE)
			res = r.search(data)
			out = res.group(1)
			r2 = re.compile("CLIENT_NAME: (.*?)$", re.MULTILINE)
			res2 = r.search(data)
			out2 = res2.group(1)
			room = self.chatrooms[out]
			room_id = room.room_id
			join_id = room.join_room(request, out2)
			response = "JOINED_CHATROOM: {0}\nSERVER_IP: {1}\nPORT: {2}\nROOM_REF: {3}\nJOIN_ID: {4}".format(out, HOST, PORT, room_id, join_id)
			request.sendto(response, client_address) 
		

	def shutdown(self):
		server.server_close()
		#Force shutdown, this is the only method which works
		os._exit(os.EX_OK)


class ThreadedRequestHandler(SocketServer.BaseRequestHandler):
	pass

	#Open a thread for each client and handle requests
	"""	
	def handle(self):
		data = self.request.recv(1024)
		curr_thread = threading.current_thread()
		response = "{} - {}".format(curr_thread.name, data)
		self.request.sendall(response)
	"""

class Server(ThreadPoolMixIn, SocketServer.TCPServer):
	pass

if __name__ == "__main__":

	HOST = "0.0.0.0"
	PORT = int(sys.argv[1])
	server = Server((HOST, PORT), ThreadedRequestHandler)
	print "Server started - ", HOST, PORT 
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		server.shutdown()

