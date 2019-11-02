import time
import cv2
import mss
import numpy


def median_color(img, kernel):
    median = cv2.medianBlur(img, kernel)
    return median


def segmentation_color(img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # COLORPICKER = [105   8 192] [ 95  -2 152] [115  18 232]
    floor_low = numpy.array([75, 0, 145])
    floor_high = numpy.array([125, 25, 255])
    curr_mask = cv2.inRange(hsv_img, floor_low, floor_high)
    hsv_img[curr_mask > 0] = ([0, 0, 0])
    img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
    return img


def gray_converting(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img_gray


def thresholding_white_black(img):
    # ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    return thresh


def edge_filtering(img, img_src):
    img, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    return img, img_src


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


def underlining(img):
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
        img_src = numpy.array(sct.grab(monitor))

        # Display the picture
        # cv2.imshow("OpenCV/Numpy normal", img)

        img = segmentation_color(img_src)
        img = gray_converting(img)
        img = median_color(img, 13)
        img = thresholding_white_black(img)
        img = masking_top_screen(img, monitor)
        img, img_src = edge_filtering(img, img_src)

        cv2.imshow('DEEPDART Visual', img)

        # print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
