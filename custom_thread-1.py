import car_module as car
import servo_module as servo
import myo_interface_module as myo

import threading
from time import sleep
from time import time as current_time
import math
import cv2

class WhileTrueThread(threading.Thread):
    def __init__(self, interval = 0):
        threading.Thread.__init__(self)
        self.__interval = interval
        self.__stop = False
    def stop(self):
        self.__stop = True
    def _prepare(self):
        pass
    def _end(self):
        pass
    def run(self):
        self._prepare()

        while not self._stop :
            self._loop()
            sleep(self._interval)
        self._end()


class CarThread(WhileTrueThread):
    def __init__(self, control_values):
        WhileTrueThread.__init__(self, 0.1)
        self.__control_values = control_values
    def _loop(self):
        control_values = self.__control_values
        current_direction = control_values.get_current_direction()
        current_duty_cycle = control_values.get_current_duty_cycle()
        if(current_direction == 'stop'):
            car.stop()
        if(current_direction == 'forward'):
            car.move_forward(current_duty_cycle)
        if(current_direction == 'backward'):
            car.move_backward(current_duty_cycle)
        if(current_direction == 'left'):
            car.turn_left(current_duty_cycle)
        if(current_direction == 'right'):
            car.turn_right(current_duty_cycle)
        else:
            pass
                
class ServoThread(WhileTrueThread):
    def __init__(self, control_values):
        WhileTrueThread.__init__(self, 0.1)
        self.__control_values = control_values
        
    def _loop(self):
        control_values = self.__control_values
        current_horizontal_angle = control_values.get_current_horizontal_angle()
        current_vertical_angle = control_values.get_current_vertical_angle()

        servo.setHorizontalAngle(current_horizontal_angle)
        servo.setVerticalAngle(current_vertical_angle)
        
class InputThread(WhileTrueThread):
    def __init__(self, control_values):
        WhileTrueThread.__init__(self, 0.1)
        self.__control_values = control_values
    def _loop(self):
        detected_status = myo.get_current_status()
        if(detected_status == 'forward'):
            self.__control_values.set_direction('forward')
        if(detected_status == 'stop'):
            self.__control_values.set_direction('stop')
        if(detected_status == 'backward'):
            self.__control_values.set_direction('backward')
        if(detected_status == 'left'):
            self.__control_values.set_direction('left')
        if(detected_status == 'right'):
            self.__control_values.set_direction('right')
        else:
            pass
        
