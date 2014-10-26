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
import time, subprocess, random, thread
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


def blink(tiempo): 
  GPIO.output(GPIO_LED, True)
  time.sleep(tiempo)
  GPIO.output(GPIO_LED, False)
  time.sleep(tiempo)

def audio(numero):
        
  mp3="/home/pi/Calabaza/"+str(numero)+".mp3"
  subprocess.call(["mplayer", mp3], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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
      thread.start_new_thread(audio,(a,))
      thread.start_new_thread(blink,(0.1,))      


except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()
