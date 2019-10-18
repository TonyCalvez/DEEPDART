import rob1a_v01 as rob1a
import numpy as np
import matplotlib.pyplot as plt
import time

if __name__ == "__main__":
    rb = rob1a.Rob1A()
    rb.log_file_on()

    # loop to get 100 measurements of front sonar
    n = 100
    ts = np.zeros(n)
    loop_time = 0.100 # 100 ms (or 10 Hz)
    for i in range(n):
        t0 = time.time()
        # write here the code to put the distance measured
        # by the front sonar in ts[i]
        # ...
        print (i,ts[i]) # show the measured distance
        t1 = time.time()
        dt = loop_time - (t1-t0)
        if dt>0:
            time.sleep(dt)
        else:
            print ("overtime !!")
        
    rb.stop()
    rb.log_file_off()
    rb.full_end()

    # compute the mean value of the 100 measurements
    # ...
    
    # define theoretical distance to the front obstacle
    # ...
    
    # compute the bias
    # ...

