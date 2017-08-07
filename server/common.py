try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)

right_pin = 25
left_pin = 23
hard_pin = 24
fwd_pin = 17
back_pin = 18
