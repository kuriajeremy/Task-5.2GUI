import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# pins setup
living_room = 18   # PWM compatible pin
bathroom    = 15
closet      = 16

GPIO.setup(living_room, GPIO.OUT)
GPIO.setup(bathroom,    GPIO.OUT)
GPIO.setup(closet,      GPIO.OUT)

# PWM setup
pwm = GPIO.PWM(living_room, 1000)
pwm.start(0)

# turn off all
def turn_off_all():
    GPIO.output(bathroom, GPIO.LOW)
    GPIO.output(closet, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

# radio button logic
def update_leds():
    selected = room_var.get()
    turn_off_all()

    if selected == "living_room":
        update_brightness(slider.get())

    elif selected == "bathroom":
        GPIO.output(bathroom, GPIO.HIGH)

    elif selected == "closet":
        GPIO.output(closet, GPIO.HIGH)

# slider function
def update_brightness(value):
    if room_var.get() == "living_room":
        pwm.ChangeDutyCycle(float(value))

# exit
def on_exit():
    pwm.stop()
    GPIO.cleanup()
    root.destroy()

# GUI
root = tk.Tk()
root.title("Light Intensity Controller")
root.geometry("350x320")

room_var = tk.StringVar(value="")

tk.Label(root, text="Select Room").pack()

tk.Radiobutton(root, text="Living Room", variable=room_var,
               value="living_room", command=update_leds).pack()

tk.Radiobutton(root, text="Bathroom", variable=room_var,
               value="bathroom", command=update_leds).pack()

tk.Radiobutton(root, text="Closet", variable=room_var,
               value="closet", command=update_leds).pack()

# slider (0–100)
tk.Label(root, text="Living Room Brightness").pack()

slider = tk.Scale(root, from_=0, to=100,
                  orient="horizontal",
                  command=update_brightness)
slider.pack()

tk.Button(root, text="Exit", command=on_exit, bg="red").pack(pady=10)

root.mainloop()