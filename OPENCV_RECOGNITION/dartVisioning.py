import cv2
import numpy

class dartVisioning():

    def __init__(self):
        self.monitor = {"top": 120, "left": 60, "width": 800, "height": 400}
        self.kernel = 25
        self.img_src = numpy.zeros(shape=[self.monitor["top"],self.monitor["left"], 3], dtype=numpy.uint8)
        self.img_cv = numpy.zeros(shape=[self.monitor["top"], self.monitor["left"], 3], dtype=numpy.uint8)
        pass

    def findingRoad(self, img):
        self.img_src = img
        self.img_cv = img
        self.img_cv = self.segmentation_color(self.img_cv)
        self.img_cv = self.median_color(self.img_cv, self.kernel)
        self.img_cv = self.gray_converting(self.img_cv)
        self.img_cv = self.masking_top_screen(self.img_cv, self.monitor)
        self.img_cv = self.thresholding_white_black(self.img_cv)
        self.img_cv = self.edge_filtering(self.img_cv)
        self.img_src = self.underlining(self.img_cv, self.img_src, self.monitor)
        return self.img_src

    def segmentation_color(self, img):
        hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        # COLORPICKER = [105   8 192] [ 95  -2 152] [115  18 232]
        floor_low = numpy.array([60, 0, 145])
        floor_high = numpy.array([130, 40, 255])
        curr_mask = cv2.inRange(hsv_img, floor_low, floor_high)
        hsv_img[curr_mask > 0] = ([0, 0, 255])
        img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
        return img

    def median_color(self, img, kernel):
        median = cv2.medianBlur(img, kernel)
        return median

    def gray_converting(self, img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        return img_gray

    def masking_top_screen(self, img, monitor):
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

    def thresholding_white_black(self, img):
        ret, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
        # ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
        return thresh

    def edge_filtering(self, img):
        # Smoothing without removing edges.
        bilateral_images = cv2.bilateralFilter(img, 7, 50, 50)

        # Applying the canny filter
        canny_images = cv2.Canny(bilateral_images, 60, 120)
        return canny_images

    def underlining(self, img, img_src, monitor):
        edges = cv2.Canny(img, 75, 150)

        lines = cv2.HoughLinesP(edges, 1, numpy.pi / 180, 25, maxLineGap=255)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                if x1 < monitor["width"] / 8 or x1 > monitor["width"] - monitor["width"] / 8:
                    cv2.line(img_src, (x1, y1), (x2, y2), (0, 255, 0), 10)
        return img_src

