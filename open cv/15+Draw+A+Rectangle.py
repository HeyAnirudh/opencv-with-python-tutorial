import cv2 as cv

img = cv.imread("lena.jpg", 1)

#img = cv.rectangle(img, (100, 100), (512, 200), (0, 0, 255), thickness=7)

#Fill a rectangle
img = cv.rectangle(img, (100, 100), (512, 200), (0, 255, 0), -1)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()