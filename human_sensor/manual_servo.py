import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

p1 = GPIO.PWM(13, 50)
p2 = GPIO.PWM(27, 50)

p1.start(0.0)
p2.start(0.0)

while True:
    try:
        a = []
        a = input("input degrees (-90 ~ 90):").split()
        
        if a[0] == "set":
            dc1 = float(0.0)
            dc2 = float(0.0)
        else:
            dc1 = 2.5 + (12.0 - 2.5) / 180 * (float(a[0]) + 90)
            dc2 = 2.5 + (12.0 - 2.5) / 180 * (float(a[1]) + 90)

        print(f"  dc1 = {dc1}")
        print(f"  dc2 = {dc2}")

        p1.ChangeDutyCycle(dc1)
        time.sleep(0.3)
        p1.ChangeDutyCycle(7.25)
        time.sleep(0.3)
        p1.ChangeDutyCycle(0.0)
        time.sleep(0.3)

        p2.ChangeDutyCycle(dc2)
        time.sleep(0.3)
        p2.ChangeDutyCycle(7.25)
        time.sleep(0.3)
        p2.ChangeDutyCycle(0.0)
        time.sleep(0.3)
    except:
        print("Exception happened!")
        p1.stop()
        p2.stop()
        GPIO.cleanup()
        exit()
    

