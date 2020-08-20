#!/usr/bin/python3
# License : GPL v3.0
# Created by Saman Ebrahimnezhad .
#
# This script will connect to the server and will save the downloaded file.
# You can use this script personally but pay attention to the license file.

import socket
import signal
import sys
import os

class NetgetClient:
	"""This is the main class of the client program."""

	def __init__(self):

		if len(sys.argv) > 2 and str(sys.argv[1]) != __file__: # this condition checks the script's arguments.

			try:

				self.sock = socket.socket()
				self.sock.connect((str(sys.argv[1]), 7575))

			except:
				print("[\033[0;31m-\033[0m] Error in connecting to the server...")
				sys.exit(1)

			signal.signal(signal.SIGINT, self.ctrlC) # if user sends SIGINT (same as ^C) signal ctrlC method will be called.

			self.download()

		else:
			print("Usage: client.py SERVER_IP_ADDRESS FILENAME")

	def download(self):
		"""This method will download and save the file."""

		print("[\033[0;32m+\033[0m] Downloading the file...")

		try:

			self.theFile = open("./" + str(sys.argv[2]), 'wb') # this line opens the file that you told the script (binary).

		except:

			print("[\033[0;31m-\033[0m] Error in writing the file...")

		p = self.sock.recv(4096)

		while p:
			self.theFile.write(p)
			p = self.sock.recv(4096)

		self.theFile.close()
		self.sock.close()

		print("[\033[0;32m+\033[0m] Download completed!")

		sys.exit(0)

	def ctrlC(self, sig, frame):
		"""This method can cancel the downloading."""

		ans = input("Do you want to cancel the downloading file? [y,N]> ")

		if str(ans).lower() == 'y':

			# Cancel the downloading

			os.remove("./" + str(sys.argv[2]))
			self.sock.close()
			self.theFile.close()
			sys.exit(1)

if __name__ == '__main__':
	netget_client = NetgetClient()