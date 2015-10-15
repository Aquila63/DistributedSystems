Distributed Systems Lab II - Multithreaded Server w/ Thread Pooling

Usage -> ./start.sh [port number]

14/10

There are several issues with this version:

* The server can't be killed through normal means, it has to be killed with a "kill command" like SIGKILL/SIGSEGV. Not really sure why the serve_forever loop is so hard to kill; SocketServers are pretty confusing though, nor is Python really suited for multi-threading.

* The bash file provided should work, but I've had problems with the client. Sometimes the clients will return a "Connection Refused" error, which implies that the server isn't there or running, which isn't right. 
No idea how to fix that, it works sometimes. I realize that the system is automated at some stage, I just hope that someone reads this README if it doesn't 
work

* The Client IPs don't come out right, it's printing the local address instead.



