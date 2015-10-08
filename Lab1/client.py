import socket

def send_local_request(host, port):
	#Initalize socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#Connect to provided host
	sock.connect((host, port))
	#Set the timeout time to 1 second
	sock.settimeout(1.0)
	#Send the server a HTTP GET request 
	sock.send("GET /echo.php HTTP/1.0\r\n\r\n")
	#Recieve data send back by the server
	recv_data = sock.recv(1000)
	#Print it to the screen
	print recv_data
	#Close the connection/socket
	sock.close()

send_local_request("localhost", 8000)
