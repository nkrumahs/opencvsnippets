import cv2
import numpy

image = cv2.imread("ve.png", cv2.IMREAD_COLOR)
# cv2.imshow("color detector", image)
cv2.waitKey(0)


lower = numpy.array([255, 255, 255], dtype="uint8")
upper = numpy.array([255, 255, 255], dtype="uint8")

# lower = numpy.array([17, 15, 100], dtype="uint8")
# upper = numpy.array([50, 56, 200], dtype="uint8")

mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("all yellow", numpy.hstack([image, output]))
cv2.waitKey(0)
