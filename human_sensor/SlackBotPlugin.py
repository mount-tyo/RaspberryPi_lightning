# coding: utf-8

from slackbot.bot import respond_to, listen_to, default_reply

from config import *
import servo

# 「電気点けて」「light on」等に反応するようにします
@listen_to('電気点けて')
@listen_to('でんきつけて')
@listen_to('light on')
@respond_to('電気点けて')
@respond_to('でんきつけて')
@respond_to('light on')
def onLight(message, *something):
    message.reply('わかりました。電気点けます。')
    servo.switch_on()


# 「電気消して」「light off」等の場合はこちら
@listen_to('電気消して')
@listen_to('でんきけして')
@listen_to('light off')
@respond_to('電気消して')
@respond_to('でんきけして')
@respond_to('light off')
def offLight(message, *something):
    message.reply('わかりました。電気消します。')
    servo.switch_off()
