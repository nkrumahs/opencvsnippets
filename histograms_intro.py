import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = np.zeros((100, 100), np.uint8)
# cv2.rectangle(img, (0, 50), (100, 100), (255), -2)
# cv2.circle(img, (50, 50), 25, 127, -1)

img = cv2.imread("lena.jpg")
b, g, r = cv2.split(img)
# cv2.imshow("blue", b)
# cv2.imshow("green", g)
# cv2.imshow("red", r)


cv2.imshow("img", img)

# plt.hist(img.ravel(), 256, [0, 256])
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.show()
