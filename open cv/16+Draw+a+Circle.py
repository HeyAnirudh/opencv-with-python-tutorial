import cv2 as cv

img = cv.imread("lena.jpg", 1)

#img = cv.circle(img, (255, 255), 100, (0, 255, 0), thickness=7)

img = cv.circle(img, (460, 50), 50, (0, 255, 0), -1)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()