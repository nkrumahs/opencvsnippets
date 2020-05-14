import cv2
import numpy
import win32api
# import win32con

winname = "Dext IWB"
winRed = "Red"
winGray = "Grayscale"
cap = cv2.VideoCapture(1)
threshHold = 255

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("55", frame)
        if cv2.waitKey(1) == 27:
            break

        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(grayframe)
        if(maxVal == threshHold):
            cv2.circle(grayframe, maxLoc, 20, (255, 0, 0))
            cv2.putText(grayframe, str(maxVal), maxLoc,
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0))
            win32api.SetCursorPos(maxLoc)

        cv2.imshow(winname, grayframe)
        if cv2.waitKey(1) == 27:
            winname = winGray
            break
    else:
        break


cap.release()
cv2.destroyWindow(winname)
