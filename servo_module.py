import RPi.GPIO as GPIO
import time
servoPin1 = 17
servoPin2 = 27
GPIO.setmode(GPIO.BCM)

GPIO.setup(servoPin1, GPIO.OUT)
GPIO.setup(servoPin2, GPIO.OUT)
p1 = GPIO.PWM(servoPin1, 50) # GPIO 17 for PWM with 50Hz
p2 = GPIO.PWM(servoPin2, 50) # GPIO 27 for PWM with 50Hz
p1.start(2.5) # Initialization
p2.start(2.5) # Initialization


def setAngle(pin,angle,pwm):
    GPIO.setmode(GPIO.BCM)
    duty = angle / 18 + 2
    GPIO.output(pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(pin, False)
    pwm.ChangeDutyCycle(0)
    
def setHorizontalAngle(angle):
    if(angle < 15):
        angle = 0
    if(angle > 160):
        angle  = 160
    setAngle(servoPin2, angle, p2)
  
def setVerticalAngle(angle):
    if(angle < 0):
        angle = 0
    if(angle > 90):
        angle = 90
    setAngle(servoPin1, angle, p1)
  
# Servo vertical orientation should be in range of 0-90
# Servo horizontal orientation should be in raqnge of 15-165
def set_default_angle():
    try:
        setHorizontalAngle(80)
        setVerticalAngle(0)
    except Exception as e:
        print(e)

def deinit_servo():
    p1.stop()
    p2.stop()
    GPIO.cleanup()
