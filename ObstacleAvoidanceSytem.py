import RPi.GPIO as GPIO # import rpi.gpio library to initiliaze the gpio number

obstaclePin=7 # initialize the pin number physical location on board
def setup(): # function to initialize the board and provide gpio pin location
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(obstaclePin,GPIO.IN,pull_up_down=GPIO.PUD_UP) #used for 3.3v to be high
def loop_for_sensor():
    while True:
        if(0== GPIO.input(obstaclePin)): # if barrier came then input from sensor is zero
            print("Barrier is detected !") # print when obstacle detected
            
def destroy():
    GPIO.cleanup() # destroy all the resouces assigned like pin number alloted
if __name__=="__main__":
    setup()
    try:
        loop_for_sensor()
    except KeyboardInterrupt: # ctrl + c will interrupt the programme
        destroy()
    