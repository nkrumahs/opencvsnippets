import cv2

winname = "Dext IWB"
cap = cv2.VideoCapture(1)
threshHold = 255

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # grayframe = frame[:, :, 1]
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(grayframe)
        if(maxVal=threshHold):
            cv2.circle(grayframe, maxLoc, 20, (255, 0, 0))
            cv2.putText(grayframe, str(maxVal), maxLoc,
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0))

        cv2.imshow(winname, frame)
        cv2.imshow(winname, grayframe)
        if cv2.waitKey(1) == 27:
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
