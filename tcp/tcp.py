import socket
import sqlite3
import logging
import os
from time import sleep
import sys

# DB
conn = sqlite3.connect('events.db')
c = conn.cursor()

# Logging
logger = logging.getLogger('timeseries')
hdlr = logging.FileHandler(os.getcwd()+'/error_log.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

# Data Point
class Event():
	# Time Series data
	def __init__(self, timestamp, value):
		self.timestamp = timestamp
		self.value = value

	# Insert data into DB
	def insertData(self):
		try:
			c.execute("INSERT INTO events (timestamp, value) VALUES (?, ?)", (self.timestamp, self.value))
			conn.commit()
			print((self.timestamp, self.value))
		except (sqlite3.Error, OverflowError) as e:
			_data = ' '.join([str(self.timestamp), str(self.value)])
			logger.error(e)
			logger.info(_data)
			print('Error: ', e)
			print('Data: ', _data)


# Stream Listener
class TimeSeriesStreamListener():

	def __init__(self, TCP_IP='tools-cluster-01.tulipintra.net', TCP_PORT=3333):
		self.TCP_IP = TCP_IP
		self.TCP_PORT = TCP_PORT
		self.BUFFER_SIZE = 1

	def listen(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect((self.TCP_IP, self.TCP_PORT))

		bracket_stack = []
		comma_stack = []
		ts = ''
		val = ''
		while True:
			try:
				data = s.recv(self.BUFFER_SIZE).decode('UTF-8')
				if not data: break

				# if stack is empty
				if not bracket_stack:
					# if you encounter a '['
					if data == '[':
						bracket_stack.append(data)
				else:
					if data == ']':
						# reset stacks
						bracket_stack.pop()
						comma_stack.pop()

						# commit to database
						event = Event(int(ts),int(val))
						event.insertData()

						# reset data buffers
						ts = ''
						val = ''
					elif data == ',' and not comma_stack:
						comma_stack.append(data)
					elif data.isdigit() and comma_stack:
						val += data
					elif data.isdigit() and not comma_stack:
						ts += data
			except socket.timeout as e:
				# sleep(2)
				logger.info('socket timed out, retrying')
				# continue
				break
			except socket.error as e:
				logger.error(e)
		s.close()
		return True

if __name__ == '__main__':
	# Run the stream
	while True:
		TimeSeriesStreamListener().listen()
