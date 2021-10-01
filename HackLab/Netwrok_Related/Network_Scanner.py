#!/bin/python3

import sys
import socket
from datetime import datetime as dt
import optparse

# Define our target
parse = optparse.OptionParser()
parse.add_option("-T", "--Target", dest="target", help="Host name")
parse.add_option("-p", "--Port", dest="port", help="Port number")
(options, arguments) = parse.parse_args()
target = options.target
port = int(options.port)

# Add a pretty banner
print("-" * 50)
print("Scanning target" + target)
print("Time Started: " + str(dt.now()))
print("-" * 50)

try:
    for port in range(0, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # returns as error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program")
sys.exit()
