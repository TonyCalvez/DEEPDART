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

def masking_top_screen(img, monitor):
    vertices = numpy.array([[0, monitor["height"]], [0, monitor["height"]/2], [monitor["width"]/3, monitor["height"]/3], [2*monitor["width"]/3, monitor["height"]/3], [monitor["width"], monitor["height"]/2], [monitor["width"], monitor["height"], ],
                            ], numpy.int32)
    mask = numpy.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, [vertices], 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked

def Ylines(img):
    graysrc = cv2.GaussianBlur(img, (3, 3), 0)
    grady = cv2.Sobel(graysrc, cv2.CV_16S, 0, 1, ksize=3, scale=1, delta=0)
    grady = cv2.convertScaleAbs(grady)
    return grady

def tracing_the_road(img):
    lines = cv2.HoughLines(img, rho=1, theta=numpy.pi / 180, threshold=100)
    if lines is not None :
        for rho, theta in lines[0]:
            a = numpy.cos(theta)
            b = numpy.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow('DEEPDART Visual', img)


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
        img = masking_top_screen(img, monitor)
        img = Ylines(img)
        tracing_the_road(img)
        #cv2.imshow('DEEPDART Visual', img)

        # print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
