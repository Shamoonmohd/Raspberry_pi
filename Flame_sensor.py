import RPi.GPIO as GPIO

Flame_sensor_pin = 7
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Flame_sensor_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    
def loop():
    while(True):
        if GPIO.input(Flame_sensor_pin)== GPIO.HIGH:
            print("Flame detected")
        
def destroy():
    GPIO.cleanup()

if __name__=="__main__":
    setup()
    try:
        loop()
    except:
        destroy()