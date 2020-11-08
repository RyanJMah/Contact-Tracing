import os
import re
import queue
import threading
import subprocess

class BLE_Tracker(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

		self.p1 = None
		self.p2 = None

		self.running = True
		self.out_buffer = queue.Queue()

	def _decode_response(self, response):
		ret = re.findall("Device .*RSSI.*\n", response)
		ret = [s[:len(s)-1] for s in ret]
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

	def run(self):
		self.start_subprocesses()

		for r in iter(self.p1.stdout.readline, ""):
			if not(self.running):
				break

			response = r.decode()
			if self._decode_response(response) != []:
				self.out_buffer.put(self._decode_response(response))

	def stop(self):
		self.kill_subprocesses()
		self.running = False


def main():
	tracker = BLE_Tracker()
	tracker.start()

	try:
		while True:
			if not(tracker.out_buffer.empty()):
				print(tracker.out_buffer.get())

	except KeyboardInterrupt:
		tracker.stop()


	exit()


if __name__ == "__main__":
	main()
