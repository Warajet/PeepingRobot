from request_cam_position import Camera_requestor
import servo_module as servo
from time import sleep
import os


class Servo:
    def __init__(self, control_values):
        self.__control_values = control_values
        self.horizontal_angle = 80
        self.vertical_angle = 0
        servo.set_default_angle()

        self.cam_requestor = Camera_requestor()
        
    def loop(self):
        self.cam_requestor.request_yz_data()

        print("Entered Servo Thread Loop")
        self.horizontal_angle = self.cam_requestor.get_Z() + 80
        self.vertical_angle = self.cam_requestor.get_Y()
        servo.setHorizontalAngle(self.horizontal_angle)
        servo.setVerticalAngle(self.vertical_angle)

def deinit_modules():
    servo.deinit_servo()

def main():
    servo1 = Servo(None)
    while True:
        servo1.loop()
        sleep(0.01)

if __name__ == '__main__':
    main()
