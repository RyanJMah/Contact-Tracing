import os
import re
import threading
import queue
import subprocess

class _scan_BLE_thread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

		self.out_pipe = queue.Queue()	
		self.running = True
		self.daemon = True

	def _decode_response(self, response):
		ret = re.findall("Device .*RSSI.*\n", response).group()
		ret = [s[:len(s)-1] for s in ret]
		return ret		

	def run(self):
		os.system("bluetoothctl > pipe")
		while(True):
			if not(self.running):
				break

			with open("pipe", "r") as f:
				response = self._decode_response(f.read())

			self.out_pipe.put(response)

			with open("pipe", "w") as f:
				f.write("")


class BLE_Tracker():
	def __init__(self):
		self.scanner_thread = None

	def get_device_info(self):
		if self.scanner_thread is None:
			throw(ValueError)
		else:
			while self.scanner_thread.out_pipe.is_empty():
				pass

			self.scanner_thread.out_pipe.get()

	def start(self):
		self.scanner_thread = _scan_BLE_thread()
		self.scanner_thread.start()

	def stop(self):
		self.scanner_thread.running = False


def main():
	tracker = BLE_Tracker()
	tracker.start()

	while True:
		print(tracker.get_device_info())



if __name__ == "__main__":
	main()

