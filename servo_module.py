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
    duty = angle / 18 + 2
    GPIO.output(pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(pin, False)
    pwm.ChangeDutyCycle(0)
    
def setHorizontalAngle(angle):
  setAngle(servoPin2, angle, p2)
  
def setVerticalAngle(angle):
  setAngle(servoPin1, angle, p1)
  
# Servo vertical orientation should be in range of 0-90
# Servo horizontal orientation should be in raqnge of 15-165
def main():
  try:
    setHorizontalAngle(15)
    setVerticalAngle(0)
    while True:
      i = int(input("Enter Vertical degree: "))
      setVerticalAngle(i)
      j = int(input("Enter Horizontal degree: "))
      setHorizontalAngle(j)

  except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
main()
