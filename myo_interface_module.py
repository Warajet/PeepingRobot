import sys
sys.path.append('../lib/')

from device_listener import DeviceListener
from pose_type import PoseType

from myo import Myo
from vibration_type import VibrationType

print("Start of myo_interface_module")
myo = Myo()
listener = PrintPoseListener()

def connect_myo(control_values):
    try:
        myo.connect()
        listener.set_control_values(control_values)
        myo.add_listener(listener)
        myo.vibrate(VibrationType.SHORT)
    except Exception as ex:
        print(ex)

def detect_myo_pose():
    myo.run()

def deinit_myo():
    myo.safely_disconnect()
    print("Finished")
    
