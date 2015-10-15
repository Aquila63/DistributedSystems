#!/bin/bash
xterm -hold -e "python threaded_server.py $1" &
sleep 2 & #This is screwed up, sometimes the clients think the server isn't running
xterm -hold -e "python clients.py $1" 