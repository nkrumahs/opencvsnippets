import cv2

winname = "window"
cap = cv2.VideoCapture(1)


while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow(winname, frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
