import sys
sys.path.append('../lib/')

from device_listener import DeviceListener
from pose_type import PoseType

class PrintPoseListener(DeviceListener):
	def __init__(self):
		# self.status = "stop"
		self.cur_dir = "stop"


	def on_pose(self, pose):
		# pose_type = PoseType(pose)
		# print(pose_type.name)

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

		
