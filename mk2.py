#!/usr/bin/env python
#encoding: utf8

import pigpio, time   # ライブラリのインポート

gpio_up = 4   # LED を接続した GPIO

pi = pigpio.pi()   # GPIOにアクセスするためのインスタンスを作成
pi.set_mode(gpio_up,pigpio.OUTPUT)   # GPIO pin を出力設定

pi.write(gpio_up,1)   # フォトカプラSWON
time.sleep(0.5)       # 0.5s ウェイト
pi.write(gpio_up,0)   # フォトカプラSWOFF
pi.stop()   # pigpio リソースの開放
