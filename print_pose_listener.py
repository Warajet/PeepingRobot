import sys
import car_module as car
sys.path.append('../lib/')

from device_listener import DeviceListener
from pose_type import PoseType

class PrintPoseListener(DeviceListener):
        def __init__(self):
                self.control_values = None
                self.cur_dir = "stop"
                
        def set_control_values(self, control_values):
                self.control_values = control_values
                
        def on_pose(self,pose):
                pose_type = PoseType(pose).name                                
                if pose_type == "FIST":
                    self.cur_dir = "stop"
                elif pose_type == "WAVE_IN":
                    self.cur_dir = "left"
                elif pose_type == "WAVE_OUT":
                    self.cur_dir = "right"
                elif pose_type == "FINGERS_SPREAD":
                    self.cur_dir = "forward"
                elif pose_type == "DOUBLE_TAP":
                    self.cur_dir = "backward"
                self.control_values.set_direction(self.cur_dir)
                print("PoseType: " + pose_type)
