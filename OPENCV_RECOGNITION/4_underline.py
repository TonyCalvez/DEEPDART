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
    bilateral_images = cv2.Canny(gray_filtered, 60, 120)

    img_gauss = cv2.GaussianBlur(bilateral_images, (9, 9), 0)
    return img_gauss


def masking_top_screen(img, monitor):
    vertices = numpy.array(
        [[0, monitor["height"]], [0, monitor["height"] / 2], [monitor["width"] / 3, monitor["height"] / 3],
         [2 * monitor["width"] / 3, monitor["height"] / 3], [monitor["width"], monitor["height"] / 2],
         [monitor["width"], monitor["height"]],
         ], numpy.int32)
    mask = numpy.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, [vertices], 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked


def underline(img):
    cdst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cdstP = numpy.copy(cdst)
    lines = cv2.HoughLines(img, 1, numpy.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = numpy.cos(theta)
            b = numpy.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv2.line(cdst, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)

    linesP = cv2.HoughLinesP(img, 1, numpy.pi / 180, 50, None, 50, 10)

    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv2.LINE_AA)
    return cdstP


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
        img = underline(img)
        cv2.imshow('DEEPDART Visual', img)

        # print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
