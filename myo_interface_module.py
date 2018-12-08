import sys
sys.path.append('lib/')

from device_listener import DeviceListener
from pose_type import PoseType

from myo import Myo
from vibration_type import VibrationType

class MyoListener(DeviceListener):
    def __init__(self):
        self.current_pose = "REST"

	def on_pose(self, pose):
		cur_pose = PoseType(pose).name

		if cur_pose == "FIST":
			self.cur_dir = "stop"
		elif cur_pose == "WAVE_IN":
			self.cur_dir = "left"
		elif cur_pose == "WAVE_OUT":
			self.cur_dir = "right"
		elif cur_pose == "FINGERS_SPREAD":
			self.cur_dir = "forward"
		elif cur_pose == "DOUBLE_TAP":
			self.cur_dir = "backward"

		print("Dir: " + self.cur_dir + ", Pose: " + cur_pose)

def detected_pose():
    print("Start Myo for Linux")
    listener = MyoListener()
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
    detected_pose()
