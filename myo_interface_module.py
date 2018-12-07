import sys
sys.path.append('lib/')

from myo import Myo
from print_pose_listener import PrintPoseListener
from vibration_type import VibrationType

def detect_myo_pose():
    print("Start Myo for Linux")
    listener = PrintPoseListener()
    myo = Myo()
    try:
        myo.connect()
        myo.add_listener(listener)
        myo.vibrate(VibrationType.SHORT)
        while True:
            myo.run()
    except Exception as e:
        print(e)
    finally:
        myo.safely_disconnect()
        print("Finished")
if __name__ == '__main__':
    detect_myo_pose()
