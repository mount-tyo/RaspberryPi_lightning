import RPi.GPIO as GPIO     # GPIOを操作するためのライブラリ(必須)

# used GPIO pin number
servo_pin_1 = 17            # サーボ１へ制御信号を送るGPIOピン
servo_pin_2 = 27            # サーボ２へ制御信号を送るGPIOピン
human_sensor_pin = 25       # 人感センサからの信号を受け取るGPIOピン

# GPIO settings
GPIO.setmode(GPIO.BCM)                  # GPIOの各ピンのナンバリング設定(役割で指定) 
GPIO.setup(servo_pin_1, GPIO.OUT)       # サーボ１　　：　出力 
GPIO.setup(servo_pin_2, GPIO.OUT)       # サーボ２　　：　出力
GPIO.setup(human_sensor_pin, GPIO.IN)   # 人感センサ　：　入力

# servo motor settings.
freq = 50                               # [Hz] , PWMの周波数
p1 = GPIO.PWM(servo_pin_1, freq)        # サーボ１のPWMインスタンス
p2 = GPIO.PWM(servo_pin_2, freq)        # サーボ２のPWMインスタンス
newtral = 7.0                           # サーボがニュートラルの位置になる値
on_degree_1 = 9.0                       # サーボ１がON 動作をする値
off_degree_1 = 5.5                      # サーボ１がOFF動作をする値
on_degree_2 = 11.0                      # サーボ２がON 動作をする値
off_degree_2 = 2.5                      # サーボ２がOFF動作をする値

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
EVENT_NAME = ""       # イベント名, URLに組み込まれてる
WEBHOOK_KEY = ""      # Slackのあるchannel
