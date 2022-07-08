import RPi.GPIO as GPIO
import time               # 時間計測のため
from config import *      # 設定ファイル

class Servo:
    def __init__(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)                  # GPIOの各ピンのナンバリング設定(役割で指定) 
        GPIO.setup(SERVO_PIN_1, GPIO.OUT)       # サーボ１　　：　出力 
        GPIO.setup(SERVO_PIN_2, GPIO.OUT)       # サーボ２　　：　出力
        self.p1 = GPIO.PWM(SERVO_PIN_1, FREQ)        # サーボ１のPWMインスタンス
        self.p2 = GPIO.PWM(SERVO_PIN_2, FREQ)        # サーボ２のPWMインスタンス
        self.p1.start(0.0)
        self.p2.start(0.0)
        
    def switch_on(self):
        """Switch lab's room light to ON by servo motor.
        """
        self.p1.ChangeDutyCycle(PWM_VAL)
        time.sleep(0.4)
        self.p1.ChangeDutyCycle(SERVO_NEUTRAL)
        time.sleep(0.3)
        self.p1.ChangeDutyCycle(0.0)
      
        self.p2.ChangeDutyCycle(CPWM_VAL)
        time.sleep(0.3)
        self.p2.ChangeDutyCycle(SERVO_NEUTRAL)
        time.sleep(0.3)
        self.p2.ChangeDutyCycle(0.0)
  
    def switch_off(self):
        """Switch lab's room light to OFF by servo motor.
        """
        self.p1.ChangeDutyCycle(CPWM_VAL)
        time.sleep(0.4)
        self.p1.ChangeDutyCycle(SERVO_NEUTRAL)
        time.sleep(0.3)
        self.p1.ChangeDutyCycle(0.0)
      
        self.p2.ChangeDutyCycle(PWM_VAL+0.8)
        time.sleep(0.3)
        self.p2.ChangeDutyCycle(SERVO_NEUTRAL)
        time.sleep(0.3)
        self.p2.ChangeDutyCycle(0.0)


if __name__ == "__main__":
    s = Servo()
    input("ON")
    s.switch_on()
    input("OFF")
    s.switch_off()

