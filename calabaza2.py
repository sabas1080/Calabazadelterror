#!/usr/bin/python
# calabaza.py
# Calabaza parlanchina
# para dia de muertos.
#
# Author : Andres Sabas
# Date   : 21/10/2014
# -----------------------

# -----------------------
# Import required Python libraries
# -----------------------
import time, subprocess, random, threading, thread
import RPi.GPIO as GPIO

# -----------------------
# Define some functions
# -----------------------

def measure():
  # This function measures a distance

  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2

  return distance

def measure_average():
  # This function takes 3 measurements and
  # returns the average.

  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

class MyThread (threading.Thread):
    #def __init__(self,threadID,name,delay, counter):
    #def blink(delay):
     def __init__(self):
        threading.Thread.__init__(self)
      
        def run(self):
          GPIO.output(GPIO_LED, True)
          time.sleep(0.1)
          GPIO.output(GPIO_LED, False)
          time.sleep(0.1)

        #def audio(self):
         # a=random.randrange(1, 7, 1)
          #mp3="/home/pi/Calabaza/"+str(a)+".mp3"
          #print mp3
          #subprocess.call(["mplayer", mp3], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          #subprocess.call(["mplayer", mp3])
        
#class MyThread2 (threading.Thread):
    #def __init__(self,threadID,name,delay, counter):
    #def blink(delay):
 #    def __init__(self):
   #     threading.Thread.__init__(self)
        
  #    def run(self):
    #    a=random.randrange(1, 7, 1)
     #   mp3="/home/pi/Calabaza/"+str(a)+".mp3"
        #print mp3
      #  subprocess.call(["mplayer", mp3], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #subprocess.call(["mplayer", mp3])

def audio(numero):
        
  mp3="/home/pi/Calabaza/"+str(numero)+".mp3"
  #print mp3
  subprocess.call(["mplayer", mp3], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  #subprocess.call(["mplayer", mp3])

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24
GPIO_LED     = 22
print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
GPIO.setup(GPIO_LED,GPIO.OUT)      #Led Indicador

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  while True:

    distance = measure_average()
    if distance > 50.0:
      print "Distance : %.1f" % distance
      time.sleep(1)
    else:
      a=random.randrange(1, 7, 1)
      audio(a)
      thread1=MyThread()
      #thread2=MyThread2()
      thread1.start()
      #thread2.start()
      #thread1.join()
      #thread2.join()      


except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()
