import time
import RPi.GPIO as GPIO
import requests
from config import *
import servo


### Functions ###
def ifttt_webhook(eventid, val1 = "人がいる!", val2 = "サーボON!", val3 = None):
    """send http request to IFTTT webhook

    Args:
        eventid (str): [description]
        val1 (str, optional): ご自由に. Defaults to "人がいる!".
        val2 (str, optional): ご自由に. Defaults to "サーボON!".
        val3 (optional)     : ご自由に. Defaults to None.
    """
    payload = {'value1':val1, 'value2':val2, 'value3':val3}
    url = "https://maker.ifttt.com/trigger/" + eventid + "/with/key/" + WEBHOOK_KEY
    response = requests.post(url, data=payload)


def switch(message):
    """switchingをする関数

    Args:
        message (str): "on" => ON動作, "off" => OFF動作
    """
    global light_status
    if(message == "off"):
        servo.switch_off()
        light_status = False
    elif (message == "on"):
        servo.switch_on()
        light_status = True
    else:
        pass


def check_human_sensor():
    """人感センサから信号を受け取って処理する関数
    """
    global on_start, pre, light_time, off_start, light_off_time

    # get sensor value.
    now = GPIO.input(human_sensor_pin)
    print(now)
    
    # check OFF => ON moment. 
    if (now == True and pre == False):
        on_start = time.time()
        if off_start is not None:
            light_off_time = on_start - off_start
            print(f"light_off_time : {light_off_time}")
            off_start = None

    # check ON => OFF moment.
    elif (on_start is not None) and (now == False):
        off_start = time.time()
        if on_start is not None:
            light_time = off_start - on_start
            print("light_time : {}".format(light_time))
            on_start = None
    
    # check ON TIME
    if (on_start is not None) and (now == True):
        if (time.time() - on_start) >= TH_ON_TIME:
            if not light_status:
                print("on")
                switch("on")
                # TODO on後の動作
                on_start = None
                # ifttt_webhook(EVENT_NAME)

    # check OFF TIME
    if(off_start is not None) and (now == False):
        if(time.time() - off_start) >= TH_OFF_TIME:
            if light_status:
                print("off")
                switch("off")
                # TODO off後の動作
                off_start = None
                # ifttt_webhook(EVENT_NAME)

    # update "pre"
    pre = now



### Main ###
def main():
    while True:
        check_human_sensor()        # 人感センサ検知
        time.sleep(SLEEP_TIME)      # 検知間隔



### Test ###
if __name__ == '__main__':
  main()
