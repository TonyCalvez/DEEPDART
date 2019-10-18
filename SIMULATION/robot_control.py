import numpy as np
import time
import random

class RobotControl:
    def __init__(self):
        self.distBetweenWheels = 0.12
        self.nTicksPerRevol = 720
        self.wheelDiameter = 0.06

    def testMove(self,rb,speedLeft,speedRight,duration):
        # forward motion
        rb.set_speed(speedLeft,speedRight)
        loopIterTime = 0.050
        tStart = time.time()
        while time.time()-tStart < duration:
            time.sleep(loopIterTime) # wait 
        # stop the robot 
        rb.stop()

    def testInfiniteObstacle (self,rb):
        loopIterTime = 0.050  # duration of loop iteration 50 ms
        legTimeMax = 5.0 # always turn after 5s (even if no obsctacle)
        distObstacle = 0.3 # stops and change direction if obstacle 
                           # at less than 30 cm
        while True:  # infinite loop : stop by typing ctrl-C
            rb.set_speed(90,90)
            tStartLeg = time.time()
            while True:
                t0 = time.time()
                if time.time()-tStartLeg >= legTimeMax:
                    break
                distFront = rb.get_sonar("front")
                #print ("distFront :",distFront)
                if distFront != 0.0 and distFront < distObstacle:
                    break
                t1 = time.time()
                dt = loopIterTime - (t1-t0)
                if dt>0:
                    time.sleep(dt) # wait for end of iteration
            # in the case the robot is trapped in front of a wall
            # go back at speed 40 for 0.5 seconds 
            rb.set_speed(-40,-40)
            time.sleep (0.5)
            # set random orientation by setting rotation duration
            # minimum time is 0.2 seconds, max is 1.5 seconds
            rotationTime = 0.2+1.3*random.random()
            rotationDirection = random.random()
            if rotationDirection < 0.5:
                self.testMove(rb,40,-40,rotationTime)
            else:
                self.testMove(rb,-40,40,rotationTime)

    def inPlaceTurnRight(self, rb, ang):   # ang in degrees  
        pass     # replace with your code


    def inPlaceTurnLeft(self, rb, ang):  # ang in degrees  
        pass     # replace with your code

    def goLineOdometer(self, rb, dist, speed):  
        # dist in meter
        # speed in % (0 to 100)
        pass     # replace with your code
