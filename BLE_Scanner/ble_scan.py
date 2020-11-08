import os
import re
import queue
import time
import threading
import subprocess
import numpy as np


class BLE_Tracker(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

		self.p1 = None
		self.p2 = None

		self.running = True

		self.daemon = True
		self.out_buffer = queue.Queue()


	def _decode_response(self, response):
		raw_list = re.findall("Device .*RSSI.*\n", response)
		raw_list = [s[:len(s)-1] for s in raw_list]

		ret = []
		for raw in raw_list:
			mac_adr = raw[raw.find(" ") + 1: raw.find("RSSI") - 1]
			rssi = float(raw[raw.find("RSSI: ") + 6: len(raw)])

			ret.append({"mac_adr": mac_adr, "rssi": rssi})

		return ret


	def start_subprocesses(self):
		self.p1 = subprocess.Popen(
			["bluetoothctl", "scan", "on"],
			shell = True,
			stdout = subprocess.PIPE
		)
		self.p2 = subprocess.Popen(["bluetoothctl scan on"], shell = True, stdout = subprocess.PIPE)

	def kill_subprocesses(self):
		self.p1.terminate()
		self.p1.wait()
		self.p2.terminate()
		self.p2.wait()

		self.p1 = None
		self.p2 = None


	def run(self):
		self.start_subprocesses()
		for r in iter(self.p1.stdout.readline, ""):
			if not(self.running):
				break

			response = r.decode()
			if self._decode_response(response) != []:
				self.out_buffer.put(self._decode_response(response))


	def stop(self):
		self.running = False
		self.kill_subprocesses()



def main():
	import time

	tracker = BLE_Tracker()
	tracker.start()

	try:
		start = time.time()
		while True:

			if not(tracker.out_buffer.empty()):
				print(tracker.out_buffer.get())

			# if time.time() - start > 10:
			# 	tracker.stop()
			# 	tracker = None

			# 	os.system("sudo systemctl disable bluetooth")
			# 	os.system("sudo systemctl enable bluetooth")	

			# 	tracker = BLE_Tracker_Backend()
			# 	tracker.start()


	except KeyboardInterrupt:
		tracker.stop()


if __name__ == "__main__":
	main()

