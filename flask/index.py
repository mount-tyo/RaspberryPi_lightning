#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import servo
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Index!"

@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/light-on")
def light_on():
    #servo.switch_on()
    s.switch_on()
    return "light on"

@app.route("/light-off")
def light_off():
    #servo.switch_off()
    s.switch_off()
    return "light off"


if __name__ == "__main__":
    s = servo.Servo()
    try:
        #app.run('0.0.0.0', debug=True)
        app.run('0.0.0.0')
    except:
        s.p1.stop()
        s.p2.stop()
        servo.GPIO.cleanup()
        print("exception")
        exit()
        
