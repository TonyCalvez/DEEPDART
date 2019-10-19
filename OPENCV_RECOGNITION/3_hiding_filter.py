import time
import cv2
import mss
import numpy


def edge_filtering(img):
    # Converting the image to grayscale.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Smoothing without removing edges.
    gray_filtered = cv2.bilateralFilter(gray, 7, 50, 50)

    # Applying the canny filter
    edges = cv2.Canny(gray, 60, 120)
    bilateral_images = cv2.Canny(gray_filtered, 60, 120)

    return bilateral_images


def masking_top_screen(img):
    vertices = numpy.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500],
                            ], numpy.int32)
    mask = numpy.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 120, "left": 60, "width": 800, "height": 400}

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        # Display the picture
        # cv2.imshow("OpenCV/Numpy normal", img)

        img = edge_filtering(img)
        img = masking_top_screen(img)

        cv2.imshow('DEEPDART Visual', img)

        # print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
