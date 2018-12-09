from custom_thread import CarThread, InputThread
import car_module as car
import myo_interface_module as myo
from time import sleep
import os

def deinit_modules():
    car.deinit()
    myo.deinit_myo()

def main():
    car._init_gpio_pins()
    control_values = car.ControlValues()

    #Let the peeping car to have common control values
    input_thread = InputThread(control_values)
    car_thread = CarThread(control_values)

    input_thread.start()
    car_thread.start()

    input_thread.join()
    car_thread.stop()

    sleep(1)

    deinit_modules()

if __name__ == '__main__':
    main()
