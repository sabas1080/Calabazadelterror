#!/usr/bin/python
# calabaza.py
# Calabaza del Terror
# para dia de muertos.
#
# Author : Andres Sabas
# Date   : 21/10/2014
# -----------------------

# -----------------------
# Import required Python libraries
# -----------------------
import time, subprocess, random
import RPi.GPIO as GPIO
# -----------------------
# Define some functions
# -----------------------


def blink(diodo): 
  GPIO.output(diodo, True)
  time.sleep(0.1)
  GPIO.output(diodo, False)
  time.sleep(0.1)
  GPIO.output(diodo, True)
  time.sleep(0.1)

def audio(numero):
        
  mp3="/home/pi/Calabaza/"+str(numero)+".mp3" #Seleccionamos una de las pistas mp3 marcadas del 1 al 6
  subprocess.call(["mplayer", mp3], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #Reproducimos la pista seleccionada  
                                                                                                  #en el reproductor mplayer

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_PIR    = 18
GPIO_LED    = 22
GPIO_LED2   = 23
GPIO_LED3   = 24
GPIO_LED4   = 25

print "Iniciando..."

# Set pins as output and input
GPIO.setup(GPIO_PIR,GPIO.IN)      # PIR
GPIO.setup(GPIO_LED,GPIO.OUT)      # Led1
GPIO.setup(GPIO_LED2,GPIO.OUT)      #Led Indicador 2
GPIO.setup(GPIO_LED3,GPIO.OUT)      #Led Indicador 3
GPIO.setup(GPIO_LED4,GPIO.OUT)      #Led Indicador 3

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.

print "Buuuuu!"

try:

  while True:

    if GPIO.input(GPIO_PIR):
      a=random.randrange(1, 7, 1) #elegimos una pista para reproducir aleatoriamente
      audio(a)
    else:
      led=random.randrange(22, 26, 1) #Elegimos un led para encender y apagar aleatoriamente
      blink(led)
  

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()
