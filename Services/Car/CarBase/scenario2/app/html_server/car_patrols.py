import time
import requests
import sts

def scanSuspect():
	time.sleep(2)
        if True:
                sts.setSpeed(100)
                sts.forward()
                time.sleep(2)
                sts.stop()
		time.sleep(1)

def scenario2():
	sts.forward()
	time.sleep(5)
	sts.stop()
	scanSuspect()
	sts.backward()
	time.sleep(5)
	sts.stop()

def initiate():
	sts.forward()
	time.sleep(0.5)
	for i in range(10):	
		sts.turnLeft()
		time.sleep(0.0001)
		sts.forward()
		time.sleep(0.00003)
	while True:
		sts.forward()
		time.sleep(3)
		sts.backward()
		time.sleep(4)
