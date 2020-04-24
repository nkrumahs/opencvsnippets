import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        text = "width: " + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        text += " height: " + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        org = (480, 500)
        fontFace = cv2.FONT_HERSHEY_PLAIN
        color = (255, 255, 255)
        frame = cv2.putText(frame, text, org, fontFace, 1, color)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
