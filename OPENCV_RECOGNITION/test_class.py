import time
import mss
import numpy
import cv2
from OPENCV_RECOGNITION.dartVisioning import dartVisioning

if __name__ == '__main__':
    with mss.mss() as sct:
        view = dartVisioning()
        view.setMonitorSize({"top": 120, "left": 60, "width": 800, "height": 400})

        # SALLE DE REYNET = [111  80 168] [101  70 128] [121  90 208]
        floor_low = [100, 20, 50]
        floor_high = [140, 190, 180]
        view.setHSVColor(minHSV=floor_low, maxHSV=floor_high)

        while "Screen capturing":
            last_time = time.time()
            img_src = numpy.array(sct.grab(view.monitor))
            view.setFlux(img_src)
            view.findingRoad()
            img_src = view.getRoad()

            cv2.imshow("DEEPDART Visual", img_src)

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break