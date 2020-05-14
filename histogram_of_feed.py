from matplotlib import pyplot
import numpy
import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("kiki", frame)
        b, g, r = cv2.split(frame)
        pyplot.hist(b.ravel(), 256, [0, 256])
        pyplot.hist(g.ravel(), 256, [0, 256])
        pyplot.hist(r.ravel(), 256, [0, 256])
        pyplot.show()
        if cv2.waitKey(1) == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
