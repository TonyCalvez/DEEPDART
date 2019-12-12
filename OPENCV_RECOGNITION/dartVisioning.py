import cv2
import numpy

class dartVisioning():

    def __init__(self):
        self.monitor = {"top": 120, "left": 60, "width": 800, "height": 400}
        self.kernel = 25
        self.center = (0, 0)
        self.cap = (0, 0)
        self.img_src = numpy.zeros(shape=[self.monitor["top"], self.monitor["left"], 3], dtype=numpy.uint8)
        self.img_cv = numpy.zeros(shape=[self.monitor["top"], self.monitor["left"], 3], dtype=numpy.uint8)
        self.points = []
        self.HSV = [[60, 0, 145], [130, 40, 255]]
        self.extremepoints = []
        pass

    def setMonitorSize(self, size):
        self.monitor = size

    def setHSVColor(self, minHSV, maxHSV):
        self.HSV = [numpy.array(minHSV), numpy.array(maxHSV)]

    def getRoadDev(self):
        return self.img_cv

    def setFlux(self, img):
        self.img_src = img
        self.img_cv = img

    def findingRoad(self):
        self.segmentation_color()
        self.median_color()
        self.gray_converting()
        self.masking_top_screen()
        self.thresholding_white_black()
        # self.edge_filtering()
        self.underlining()
        self.ploting()
        self.arrow()

    def getRoad(self):
        return self.img_src

    def segmentation_color(self):
        hsv_img = cv2.cvtColor(self.img_cv, cv2.COLOR_RGB2HSV)
        curr_mask = cv2.inRange(hsv_img, self.HSV[0], self.HSV[1])
        hsv_img[curr_mask > 0] = ([0, 0, 255])
        self.img_cv = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)

    def median_color(self):
        self.img_cv = cv2.medianBlur(self.img_cv, self.kernel)

    def gray_converting(self):
        self.img_cv = cv2.cvtColor(self.img_cv, cv2.COLOR_RGB2GRAY)

    def masking_top_screen(self):
        vertices = numpy.array(
            [[0, self.monitor["height"]], [0, self.monitor["height"] / 2],
             [self.monitor["width"] / 3, self.monitor["height"] / 3],
             [2 * self.monitor["width"] / 3, self.monitor["height"] / 3],
             [self.monitor["width"], self.monitor["height"] / 2],
             [self.monitor["width"], self.monitor["height"]],
             ], numpy.int32)
        mask = numpy.zeros_like(self.img_cv)
        # fill the mask
        cv2.fillPoly(mask, [vertices], 255)
        # now only show the area that is the mask
        self.img_cv = cv2.bitwise_and(self.img_cv, mask)

    def thresholding_white_black(self):
        ret, self.img_cv = cv2.threshold(self.img_cv, 200, 255, cv2.THRESH_BINARY)
        # ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    def edge_filtering(self):
        # Smoothing without removing edges.
        self.img_cv = cv2.bilateralFilter(self.img_cv, 7, 50, 50)
        # Applying the canny filter
        self.img_cv = cv2.Canny(self.img_cv, 60, 120)

    def underlining(self):
        image, contours, hierarchy = cv2.findContours(
            image=self.img_cv,
            mode=cv2.RETR_TREE,
            method=cv2.CHAIN_APPROX_SIMPLE)
        try:
            self.points = cv2.convexHull(contours[0])
            self.contours = contours[0]
            cv2.drawContours(self.img_src, contours=[self.points], contourIdx=-1,
                             color=(255, 0, 0), thickness=2)
        except IndexError:
            pass


    def ploting(self):
        moments = cv2.moments(self.img_cv)
        try:
            area = moments["m00"]
            mean_x = int(moments["m10"] / moments["m00"])
            mean_y = int(moments["m01"] / moments["m00"])
            self.center = (mean_x, mean_y)
            cv2.circle(self.img_src, self.center, 5, (0, 0, 255), -1)

        except ZeroDivisionError:
            pass

        try :
            max = numpy.amax(self.contours, axis=0)[0]
            print(max)
            self.cap = (400, 200)
        except IndexError:
            pass

    def arrow(self):
        cv2.arrowedLine(self.img_src, self.center, self.cap, (0, 0, 255), 5)
        pass