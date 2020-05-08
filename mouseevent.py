import cv2
import numpy

winname = 'frame'

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        color = (255, 255, 255)
        imag = cv2.putText(img, strXY, (x, y), font, 1, color, 1)
        cv2.imshow(winname, img)


img = numpy.zeros((512, 412, 3))
cv2.imshow(winname, img)
cv2.setMouseCallback(winname, click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
