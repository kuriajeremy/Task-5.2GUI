import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 18
GPIO.setup(led, GPIO.OUT)

# creating the PWM object
pwm = GPIO.PWM(led, 1000)
pwm.start(0)  # start at 0 level brightness

try:
    while True:
        for duty in range(0, 101, 5):  # increase brightness
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.1)

        for duty in range(100, -1, -5):  # decrease brightness
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()