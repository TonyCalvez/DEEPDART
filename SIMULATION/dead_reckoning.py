import rob1a_v01 as rob1a  # get robot simulator
import robot_control  # get robot control functions 
import numpy as np
import time


if __name__ == "__main__":
    rb = rob1a.Rob1A()   # create a robot (instance of Rob1A class)
    ctrl = robot_control.RobotControl() # create a robot controller

    # place here your commands  to move and turn


    # safe end : stop the robot, then stop the simulator
    rb.stop()
    rb.log_file_off() # end log
    rb.full_end()
