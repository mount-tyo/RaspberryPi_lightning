# used GPIO pin number
SERVO_PIN_1 = 13            # サーボ１へ制御信号を送るGPIOピン
SERVO_PIN_2 = 27            # サーボ２へ制御信号を送るGPIOピン
HUMAN_SENSOR_PIN = 25       # 人感センサからの信号を受け取るGPIOピン

# servo motor settings.
FREQ = 50                     # [Hz], PWMの周波数
SERVO_NEUTRAL = 7.25          # サーボがニュートラルの位置になる値
SW_DEG  =  18                 # サーボが ON/OFF 動作をするDegree
PWM_VAL  = 2.5 + (12.0 - 2.5) / 180 * (float(SW_DEG) + 90)
CPWM_VAL = 2.5 + (12.0 - 2.5) / 180 * (float(-SW_DEG) + 90)
print(str(PWM_VAL) + "  " + str(CPWM_VAL))

# human sensor settings.
SLEEP_TIME = 0.1            # [sec] , 計測間隔
TH_ON_TIME = 5              # [sec] , スイッチON するON 時間のしきい値
TH_OFF_TIME = 10            # [sec] , スイッチOFFするOFF時間のしきい値
on_start = None             # OFF => ON  になった瞬間の時間
off_start = None            # ON  => OFF になった瞬間の時間
light_status = False        # True is ON, Flase is OFF.  使ってない。。。
pre = 0                     # 1 step 前の人感センサの状態 (boolean)
light_time = 0              # 人感センサの検知時間(連続でONの時間)
light_off_time = 0          # OFF => ON になった瞬間の時間

# webhook settings.
EVENT_NAME = ""                  # イベント名, URLに組み込まれてる
WEBHOOK_KEY = ""      # Slackのあるchannel
