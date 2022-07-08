from RPi.GPIO import GPIO
import time
form config import *

class HumanSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(HUMAN_SENSOR_PIN, GPIO.IN)
        
    def run(self):
        pass


if __name__ == "__main__":
    pass