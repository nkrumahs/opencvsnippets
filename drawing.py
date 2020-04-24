import numpy as np
import cv2


def rgb(red, greed, blue):
    return (blue, greed, red)


# img = cv2.imread('sampledata/lena.jpg', cv2.IMREAD_COLOR)

img = np.zeros([512, 512, 3])

img = cv2.line(img, (125, 77), (125, 255), rgb(0, 0, 255), 3)
img = cv2.arrowedLine(img, (0, 77), (125, 0), rgb(255, 0, 255), 5)
img = cv2.rectangle(img, (100, 100), (400, 400), rgb(255, 125, 0), 3)
img = cv2.circle(img, (255, 255), 70, rgb(100, 255, 100), 2)
img = cv2.putText(img, "lena", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, rgb(
    255, 255, 255), 2)
print()

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows
