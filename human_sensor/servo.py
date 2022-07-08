import time             # 時間計測のため
from config import *    # 設定ファイル


def switch_on():
  """サーボで照明スイッチON
  """
  p1.start(newtral)
  #p2.start(newtral)
  p1.ChangeDutyCycle(on_degree_1)
  #p2.ChangeDutyCycle(on_degree_2)
  time.sleep(0.3)
  p1.ChangeDutyCycle(newtral)
  #p2.ChangeDutyCycle(newtral)
  time.sleep(0.3)
  #p2.stop()

def switch_off():
  """サーボで照明スイッチOFF
  """
  p1.start(newtral)
  #p2.start(newtral)
  p1.ChangeDutyCycle(off_degree_1)
  #p2.ChangeDutyCycle(off_degree_2)
  time.sleep(0.3)
  p1.ChangeDutyCycle(newtral)
  #p2.ChangeDutyCycle(newtral)
  time.sleep(0.5)
  #p1.stop()
  #p2.stop()



if __name__ == "__main__":
  input("on します")
  switch_on()
  input("off します")
  switch_off()

