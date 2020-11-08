from ble_scan import *
import sys

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.insert(1, f"{PARENT_DIR}/database")
from sql import *

def check_dis():

    tracker = BLE_Tracker()
    tracker.start()

    try:
        while True:
            if not(tracker.out_buffer.empty()):
                print(tracker.out_buffer.get())

    except KeyboardInterrupt:
        tracker.stop()

    exit()

    return

check_dis()
