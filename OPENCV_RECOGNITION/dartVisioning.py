import cv2
import numpy

class dartVisioning():

    def __init__(self):
        self.monitor = {"top": 120, "left": 60, "width": 800, "height": 400}
        self.kernel = 25
        self.img_src = numpy.zeros(shape=[self.monitor["top"],self.monitor["left"], 3], dtype=numpy.uint8)
        self.img_cv = numpy.zeros(shape=[self.monitor["top"], self.monitor["left"], 3], dtype=numpy.uint8)
        pass

    def setMonitorSize(self, size):
        self.monitor = size

    def setFlux(self, img):
        self.img_src = img
        self.img_cv = img

    def findingRoad(self):
        self.segmentation_color()
        self.median_color()
        self.gray_converting()
        self.masking_top_screen()
        self.thresholding_white_black()
        self.edge_filtering()
        self.underlining()

    def getRoad(self):
        return self.img_src

    def segmentation_color(self):
        hsv_img = cv2.cvtColor(self.img_cv, cv2.COLOR_RGB2HSV)
        # COLORPICKER = [105   8 192] [ 95  -2 152] [115  18 232]
        floor_low = numpy.array([60, 0, 145])
        floor_high = numpy.array([130, 40, 255])
        curr_mask = cv2.inRange(hsv_img, floor_low, floor_high)
        hsv_img[curr_mask > 0] = ([0, 0, 255])
        self.img_cv = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)


    def median_color(self):
        self.img_cv = cv2.medianBlur(self.img_cv, self.kernel)


    def gray_converting(self):
        self.img_cv = cv2.cvtColor(self.img_cv, cv2.COLOR_RGB2GRAY)


    def masking_top_screen(self):
        vertices = numpy.array(
            [[0, self.monitor["height"]], [0, self.monitor["height"] / 2], [self.monitor["width"] / 3, self.monitor["height"] / 3],
             [2 * self.monitor["width"] / 3, self.monitor["height"] / 3], [self.monitor["width"], self.monitor["height"] / 2],
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
        edges = cv2.Canny(self.img_cv, 75, 150)

        lines = cv2.HoughLinesP(edges, 1, numpy.pi / 180, 25, maxLineGap=255)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                if x1 < self.monitor["width"] / 8 or x1 > self.monitor["width"] - self.monitor["width"] / 8:
                    cv2.line(self.img_src, (x1, y1), (x2, y2), (0, 255, 0), 10)

