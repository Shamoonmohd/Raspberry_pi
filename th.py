import Adafruit_DHT # library used for sensor DHT11
from Adafruit_IO import Client,Feed # library used to send data on adafruit api
import datetime 
import csv
import time
sensors = Adafruit_DHT.DHT11 # initialize the sensor (DHT11)
pin = 4 # initialize the pin number
#s=int(input("Enter the sensor number 11 or 22"))
#pin=int(input("Enter the GPIO pin number in which semsor is connected"))
ADAFRUIT_IO_KEY = "06dd36fe197c464d9c9b24ea5e01b34e" # initialize the adafruit_io_key
ADADRUIT_IO_USERNAME="shamoonmohd" # initialize the adaruit username used in adafruit api

aio = Client(ADADRUIT_IO_USERNAME,ADAFRUIT_IO_KEY) # initialize with username and object
temperature_feed = aio.feeds('temperature') # initialize the temperature feeds to send to rest api
humidity_feed = aio.feeds('humidity') # initiliaze the humidity feeds to send to rest api
while(True): #loop will run repeatedly
    humidity, temperature = Adafruit_DHT.read_retry(sensors, pin)# the adafruit will fetch temperature and humidity data
   
    aio.send(temperature_feed.key, str(temperature)) # the temperature will send to rest api
    aio.send(humidity_feed.key, str(humidity)) # the humidity data will send to rest api
    print("Temperature:{0:0.1f} , Humidity:{1:0.1f}".format(temperature,humidity))# print on console screen
    
    if temperature!= None and humidity!= None:
        Date = datetime.date.today()# fetch current 
        Time = datetime.datetime.now().time() # fetch current time
        d = Date.strftime("%d/%m/%y") # convert into string object
        t = Time.strftime("%H:%M:%S") # convert into string object
        list = [d,t,temperature,humidity] 
    with open("TempHumidityData.csv","a+") as df:
        writer = csv.writer(df,delimiter=",") # write data into csv file
        writer.writerow(list)
    time.sleep(30)