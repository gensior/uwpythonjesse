#!/usr/bin/env python
# encoding: utf-8
"""
echo_server.py

Created by Jesse Franceschini on 2011-01-15.
"""

import socket

def main():
	host = ''
	port = 50000
	backlog = 5
	size = 1024
	s = socket.socket(socket.AF_INET,
					  socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(backlog)
	while True:
		client, address = s.accept()
		data = client.recv(size)
		if data:
			client.send(data)
		client.close()


if __name__ == '__main__':
	main()

