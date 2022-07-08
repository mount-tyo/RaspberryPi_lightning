from datetime import datetime
import time
import RPi.GPIO as GPIO
import requests
import os

### Global Variables ###
WEBHOOK_GPIO_PIN = 25       # PIN NUMBER
SLEEP_TIME = 0.1            # [sec] 検知間隔
THRESHOLD_ON_TIME = 10      # [sec] イベント発生に必要なON 時間
start = None                # 感知開始時間
pre = 0                     # 1 step前のセンサのON/OFF状態
light_time = 0              # light on time
EVENT_NAME = ""             # event name(id)
LONG_SLEEP = 60             # [sec] イベント後のsleep時間
WEBHOOK_KEY = ""            # slack_webhook_key

### GPIO Settings ###
GPIO.setmode(GPIO.BCM)
GPIO.setup(WEBHOOK_GPIO_PIN, GPIO.IN) 


### Functions ###
# send http request to IFTTT webhook
def ifttt_webhook(eventid):
    payload = {'value1':"人がいる!", 'value2':datetime.now().strftime('%Y/%m/%d %H:%M:%S'), 'value3':light_time}
    url = "https://maker.ifttt.com/trigger/" + eventid + "/with/key/" + WEBHOOK_KEY
    response = requests.post(url, data=payload)


# check human_sensor output
def check_human_sensor():
    global start, pre, light_time
    # get sensor value.
    now = GPIO.input(WEBHOOK_GPIO_PIN)
    # print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "  ", end="")
    # print(now)
    # check OFF => ON moment. 
    if (now == True and pre == False):
        start = time.time()
    # check ON => OFF moment.
    if (start is not None) and (now == False):
        light_time = time.time() - start
        # print("light_time : {}".format(light_time))
        start = None
    # check whether to trigger an event.
        if light_time > THRESHOLD_ON_TIME:
            ifttt_webhook(EVENT_NAME)
            # イベント後は長めのsleep
            time.sleep(LONG_SLEEP)
    # update "pre"
    pre = now



### Main ###
def main():
    while True:
        check_human_sensor()
        time.sleep(SLEEP_TIME)



### Test ###
if __name__ == '__main__':
  main()
