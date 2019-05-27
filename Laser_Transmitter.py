import RPi.GPIO as GPIO
import time

laser_pin=7

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(laser_pin,GPIO.OUT)

def loop():
    while(True):
        GPIO.output(laser_pin,GPIO.HIGH)
        print("laser is on")
        time.sleep(0.5)
        GPIO.output(laser_pin,GPIO.LOW)
        print("laser is off")
        time.sleep(0.5)
def destroy():
    GPIO.output(laser_pin, GPIO.LOW)
    GPIO.cleanup()
    
if __name__=="__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        
    