import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.IN,GPIO.PUD_UP)

def Toki_tomare():
    while GPIO.input(27) == GPIO.LOW :
        time.sleep(0.7)
    return Toki_tomare

def Toki_Ugokidasu():
    while GPIO.input(27) == GPIO.HIGH :
        return
    
try: 
    out = GPIO.output 
    while True:     
        Toki_tomare()
        out(2,GPIO.HIGH)
        time.sleep(0.7)
        Toki_tomare()
        out(3,GPIO.HIGH)
        time.sleep(0.7)
        Toki_tomare()
        out(4,GPIO.HIGH)
        time.sleep(0.7)
        Toki_tomare()
        out(17,GPIO.HIGH)
        Toki_tomare()
        out(17,GPIO.LOW)
        time.sleep(0.7)
        Toki_tomare()
        out(4,GPIO.LOW)
        time.sleep(0.7)
        Toki_tomare()
        out(3,GPIO.LOW)
        time.sleep(0.7)
        Toki_tomare()
        out(2,GPIO.LOW)
        Toki_tomare()
        time.sleep(0.7)
        Toki_Ugokidasu()
        Toki_tomare()
        if GPIO.input(27) == GPIO.HIGH:
            Toki_Ugokidasu()
        else:
            Toki_tomare()

except KeyboardInterrupt:
    pass
          
finally: 
    GPIO.cleanup()
