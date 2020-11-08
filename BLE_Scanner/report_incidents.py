import os
import sys
import time
import queue
from uuid import getnode as get_mac
from ble_scanner import BLE_Tracker

##########################################################################################
# append the directory for sql.py and geo.py to sys.path so we can import them
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

GEOLOCATION_DIR = os.path.join(PARENT_DIR, "geolocation")
DB_DIR = os.path.join(PARENT_DIR, "database")

sys.path.append(GEOLOCATION_DIR)
sys.path.append(DB_DIR)

import geo
import sql
##########################################################################################

class Incident_Reporter():
	def __init__(self):
		self.tracker = BLE_Tracker()

		self.RSSI_THRESHOLD = -70
		self.THIS_MAC_ADR = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))

	def _interpret_rssi(self):
		bt_info_list = self.tracker.out_buffer.get()
		# print(bt_info_list)

		for bt_info in bt_info_list:
			rssi = bt_info["rssi"]
			mac_adr = bt_info["mac_adr"]

			if len(sql.read_user(mac_adr = mac_adr)) == 0:
				continue
		
			print(bt_info)
			if (rssi > self.RSSI_THRESHOLD) and (rssi != 127):			
				msg = f"Reporting incident: mac1 = {self.THIS_MAC_ADR}, mac2 = {mac_adr}, rssi = {rssi}"
				print(msg)

				location_info = geo.location()

				sql.add_incident(
					mac_adr1 = self.THIS_MAC_ADR,
					mac_adr2 = mac_adr,
					rssi = rssi,
					longitude = location_info["longitude"],
					latitude = location_info["latitude"],
					date_and_time = location_info["time"]
				)

	def stop(self):
		self.tracker.stop()

	def mainloop(self):
		self.tracker.start()
		
		start = time.time()
		while True:
			if not self.tracker.out_buffer.empty():
				self._interpret_rssi()
			
			# print(time.time() - start)
			# if (time.time() - start) > 10:
			# 	self.tracker.stop()
			# 	self.tracker = None

			# 	os.system("sudo systemtcl disble bluetooth")
			# 	os.system("sudo systemtcl enable bluetooth")

			# 	self.tracker = BLE_Tracker()
			# 	self.tracker.start()

			# 	start = time.time()



def main():
	reporter = Incident_Reporter()
	try:
		reporter.mainloop()
	except KeyboardInterrupt:
		reporter.stop()


if __name__ == "__main__":
	main()

