
# run this before run the code
# export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/Users/anya/Downloads/sdk/myo.framework

from __future__ import print_function
from myo.utils import TimeInterval
import myo
import sys


class Listener(myo.DeviceListener):

  def __init__(self):
    self.interval = TimeInterval(None, 0.01)
    self.pose = myo.Pose.rest

    self.status = "stop"

  def output(self):
    if not self.interval.check_and_reset():
      return

    print(self.pose, end='  ')
    print(self.status)

  def on_connected(self, event):
    print("Hello, '{}'!".format(event.device_name))
    event.device.vibrate(myo.VibrationType.short)
    event.device.request_battery_level()

  def on_battery_level(self, event):
    print("Your battery level is:", event.battery_level)

  def on_pose(self, event):
    self.pose = event.pose
    
    if event.pose != myo.Pose.rest:
      self.status = event.pose

    if self.pose == myo.Pose.fingers_spread:
      self.status = "forward"
    elif self.pose == myo.Pose.fist:
      self.status = "stop"
    elif self.pose == myo.Pose.double_tap:
      self.status = "backward"
    elif self.pose == myo.Pose.wave_in:
      self.status = "left"
    elif self.pose == myo.Pose.wave_out:
      self.status = "right"
    self.output()

  def on_orientation(self, event):
    self.orientation = event.orientation
    self.output()

    

if __name__ == '__main__':
  myo.init()
  hub = myo.Hub()
  listener = Listener()
  while hub.run(listener.on_event, 500):
    pass
