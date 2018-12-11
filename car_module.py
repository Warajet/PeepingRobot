from time import sleep

#initialization
default_pwm_frequency = 50
pwm_pins = dict()
pin_left_1 = 15
pin_left_2 = 13
pin_right_3 = 11
pin_right_4 = 7

def deinit():
    _cleanup_gpio()
def stop():
    _set_duty_cycle_for_pins(0,0,0,0)
def turn_left(duty_cycle):
    _set_duty_cycle_for_pins(0 , duty_cycle / 2, duty_cycle / 2, 0)
def turn_right(duty_cycle):
    _set_duty_cycle_for_pins(duty_cycle / 2, 0 , 0 , duty_cycle / 2)
     
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
    import RPi.GPIO as _GPIO
    global GPIO
    GPIO = _GPIO
    
    GPIO.setmode(GPIO.BCM)
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
        self.direction = 'stop'
        self.duty_cycle = 70
        self.horizontal_angle = 80
        self.vertical_angle = 0
        
    def set_horizontal_angle(self, angle):
        self.horizontal_angle = angle
        if(self.horizontal_angle < 15):
            self.horizontal_angle = 15
        if(self.horizontal_angle > 160):
            self.horizontal_angle = 160
            
    def set_vertical_angle(self, angle):
        self.vertical_angle = angle
        if(self.vertical_angle < 0):
            self.vertical_angle = 0
        if(self.vertical_angle > 90):
            self.vertical_angle = 90
            
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
    
    def get_current_horizontal_angle(self):
        return self.horizontal_angle
    
    def get_current_vertical_angle(self):
        return self.vertical_angle

