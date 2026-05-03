from machine import Pin, PWM
import time

# setting up led with PWM
led = Pin(15, Pin.OUT)
led = PWM(Pin(15))
led.freq(1000)  # frequency (1kHz)

# test brightness levels
while True:
    for duty in range(0, 65536, 512):  # to increase brightness
        led.duty_u16(duty)
        time.sleep(0.01)

    for duty in range(65535, 0, -512):  # to decrease brightness
        led.duty_u16(duty)
        time.sleep(0.01)