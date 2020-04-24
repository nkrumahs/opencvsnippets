import cv2

img = cv2.imread('lena.jpg', cv2.IMREAD_UNCHANGED)
print(img)
cv2.imshow('hehe', img)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
