import RPi.GPIO as GPIO
import time

led_pin = 7

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin,GPIO.OUT)

def loop():
    while(True):
        GPIO.output(led_pin,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_pin,GPIO.LOW)
        time.sleep(0.5)
        
       
def destroy():
    GPIO.output(led_pin,GPIO.LOW)
    GPIO.cleanup()
    

if __name__=="__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
  
        
        