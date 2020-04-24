import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
framewidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frameheight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
size = (framewidth, frameheight)
filename = "recorded.avi"
fps = 10.0
rec = cv2.VideoWriter(filename, 0, fourcc, fps, size, True)
print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        rec.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
cap.release()
rec.release()
cv2.destroyAllWindows


def camcapture():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        grays = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', grays)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
