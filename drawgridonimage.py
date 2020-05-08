import cv2

src = cv2.imread('lena.jpg')

stepSize = 65
k = 1
s = ''

width = src.shape[1]  # gets width
height = src.shape[0]  # gets height

i = 0
while i < height:
    cv2.line(src, (0, i), (width, i), (255, 0, 0))
    i += stepSize

i = 0
while i < width:
    cv2.line(src, (i, 0), (i, height), (0, 0, 0))
    i += stepSize

i = 0
while i < width:
    j = 0
    while j < height:
        cv2.putText(src, k, (i, j), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255, 255))
        k += 1
        j += 1
    i += stepSize

cv2.imshow('h', src)
cv2.waitKey(0)
