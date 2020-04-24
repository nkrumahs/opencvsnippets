import cv2

videocapture = cv2.VideoCapture(0)
i = 0

while True:
    ret, frame = videocapture.read()
    cv2.imshow('capture', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    elif cv2.waitKey(1) == ord('s'):
        cv2.imwrite('x1shot{}.png'.format(i), frame)
        i = i+1

videocapture.release()
cv2.destroyAllWindows
