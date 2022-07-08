# ラズパイ DX

#
## １．機能
### １．１．人感センサ ＋ サーボモータ
人感センサの検知時間を判定して、サーボモータにより照明ON/OFFを行う。
下記のコマンドで実行。
```
python3 switching.py
```
### １．２．サーボモータ ＋ slackbot
slackの特定のチャンネルに、特定のメッセージを送ると
サーボモータが動作して照明スイッチをON/OFFする。
下記のコマンドで実行。

```
python3 bot.py
```

#
## ２．プログラムの説明
### `config.py`
```
設定ファイル
```
### `sensor.py`
```
人感センサーからの入力を利用して、slackの指定チャンネルに
検出情報を送る。
```
### `servo.py`
```
サーボモータによる照明スイッチ動作のための関数ファイル
```
### `manual_servo.py`
```
サーボモータの回転角度を入力して、挙動を見るためのプログラム。
```
### `switching.py`
```
人感センサで検知して、サーボモータに照明ON/OFFの司令を出す。
```
### `bot.py`
```
slackbotで特定のメッセージを検出して、サーボモータに照明ON/OFFの
司令を出す。また、webhookでslackに通知する。
```
### `slackbot_settings.py`
```
slackbotを動かすための基本設定ファイル。
```
### `SlackBotPlugin.py`
```
slackbotのlistenやrespondに関するプログラム。
```