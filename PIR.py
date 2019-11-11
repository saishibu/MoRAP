import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setwarnings(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(3, GPIO.OUT)

while True:
	i = GPIO.input(11)
	if i == 0:
		print "No Intruders", i
	else:
		print "Intruders Found"
