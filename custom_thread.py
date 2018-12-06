import car_module as car
import servo_module as servo
import camera_module as cam

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

class ServoThread(WhileTrueThread):
    def __init__(self, control_values):
        WhileTrueThread.__init__(self, 0.1)
        self.__control_values = control_values
    def _loop(self):
        
