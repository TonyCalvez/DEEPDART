import time
import mss
import numpy
import cv2
from OPENCV_RECOGNITION.dartVisioning import dartVisioning

with mss.mss() as sct:
    view = dartVisioning()
    view.setMonitorSize({"top": 120, "left": 60, "width": 800, "height": 400})

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