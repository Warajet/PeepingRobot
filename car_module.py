from time import sleep
import RPi.GPIO as GPIO
#initialization
default_pwm_frequency = 50
pwm_pins = dict()
pin_left_1 = 123
pin_left_2 = 4324
pin_right_3 = 123324
pin_right_4 = 2134324

def deinit():
    _cleanup_gpio()
def stop():
    _set_duty_cycle_for_pins(0,0,0,0)
def turn_left(duty_cycle):
    _set_duty_cycle_for_pins(0 , duty_cycle, duty_cycle, 0)
def turn_right(duty_cycle):
    _set_duty_cycle_for_pins(duty_cycle, 0 , 0 , duty_cycle)
     
#Have split_ratio in case the user would like to gradually either move right or left    
def move_forward(duty_cycle, split_ratio = 0.5):
    if(split_ratio > 1):
        split_ratio = 1
    elif (split_ratio < 0):
        split_ratio = 0
    if(split_ratio < 0.5):
        left_ratio = split_ratio / 0.5
    else:
        left_ratio = 1

    if(split_ratio > 0.5):
        right_ratio = 1 - (split_ratio - 0.5) / 0.5
    else:
        right_ratio = 1
        
    _set_duty_cycle_for_pins(duty_cycle * left_ratio , 0, duty_cycle * right_ratio, 0)

def move_backward(duty_cycle):
    _set_duty_cycle_for_pins(0, duty_cycle, 0 , duty_cycle)

def _set_duty_cycle(pin_num, duty_cycle):
    pwm_pins[pin_num].ChangeDutyCycle(duty_cycle)
    
def _set_duty_cycle_for_pins(pin1,pin2,pin3,pin4):
    _set_duty_cycle(pin_left_1, pin1)
    _set_duty_cycle(pin_left_2, pin2)
    _set_duty_cycle(pin_right_3, pin3)
    _set_duty_cycle(pin_right_4, pin4)
    
def _cleanup_gpio():
    GPIO.cleanup()
    
def _init_pwm_pin(pin_num):
    pwm_pins[pin_num] = GPIO.PWM(pin_num, default_pwm_frequency)
    pwm_pins[pin_num].start(0)
    
def _init_output_pin(pin_num):
    try:
        GPIO.setup(pin_num, GPIO.OUT)
    except Exception as e:
        print("Car Module Error: " + e)
        
def _init_gpio_pins():
    GPIO.setmode(GPIO_BOARD)
    GPIO.setwarnings(False)

    _init_output_pin(pin_left_1)
    _init_output_pin(pin_left_2)
    _init_output_pin(pin_right_3)
    _init_output_pin(pin_right_4)

    _init_pwm_pin(pin_left_1)
    _init_pwm_pin(pin_left_2)
    _init_pwm_pin(pin_right_3)
    _init_pwm_pin(pin_right_4)

class ControlValues:
    
    def __init__(self):
        self.direction = 'none'
        self.duty_cycle = 100
        
    def set_direction(self, direction):
        self.direction = direction

    def set_duty_cycle(self, duty_cycle):
        self.duty_cycle = duty_cycle
        if(self.duty_cycle > 100):
            self.duty_cycle = 100
        if(self.duty_cycle < 0):
            self.duty_cycle  = 0
            
    def get_current_duty_cycle(self):
        return self.duty_cycle
    
    def get_current_direction(self):
        return self.direction















    
