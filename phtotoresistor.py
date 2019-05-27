import RPi.GPIO as GPIO
photoresistor_pin = 7
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(photoresistor_pin,GPIO.IN)
    
def loop():
    while(True):
        
        if(GPIO.input(photoresistor_pin)==0):
            print("Light remain same")
        else :
            print("light intensity changes")
        
            
if __name__=="__main__":
    
     setup()
     try:
         loop()
     except KeyboardInterrupt:
        GPIO.cleanup()

    