import RPi.GPIO as GPIO

metal_sensor_pin = 7
Led_pin = 5

def setup():
    GPIO.setmode(GPIO.BOARD)
#    GPIO.setup(Led_pin,GPIO.OUT)
    GPIO.setup(metal_sensor_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#    GPIO.output(Led_pin,GPIO.HIGH)
   

def loop():
    while(True):
        if  GPIO.input(metal_sensor_pin)== GPIO.HIGH:
            print("On led")
#            GPIO.output(Led_pin,GPIO.LOW)
        else:
            #GPIO.output(Led_pin,GPIO.HIGH)
            print("Off led")
            
        
       
def destroy():
    GPIO.cleanup()
    
if __name__=="__main__":
    setup()
    loop()