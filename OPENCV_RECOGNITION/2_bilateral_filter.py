import time
import cv2
import mss
import numpy


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 120, "left": 60, "width": 800, "height": 400}

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        # Display the picture
        # cv2.imshow("OpenCV/Numpy normal", img)

        # Converting the image to grayscale.
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Smoothing without removing edges.
        gray_filtered = cv2.bilateralFilter(gray, 7, 50, 50)

        # Applying the canny filter
        edges = cv2.Canny(gray, 60, 120)
        bilateral_images = cv2.Canny(gray_filtered, 60, 120)
        
        cv2.imshow('OpenCV/Numpy grayscale', bilateral_images)

        print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
