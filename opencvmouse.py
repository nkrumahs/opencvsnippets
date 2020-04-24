import cv2
import numpy as np

circles = []
winname = "opencv"


def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left Click")
        circles.append((x, y))


cap = cv2.VideoCapture(0)
cv2.namedWindow(winname)
cv2.setMouseCallback(winname, onMouse)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        for c in circles:
            cv2.circle(frame, c, 5, (0, 0, 0), 2)

        cv2.imshow(winname, frame)

        if cv2.waitKey(1) == 27:
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
