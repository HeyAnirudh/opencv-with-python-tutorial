import cv2 as cv

img = cv.imread("lena.jpg", 1)

font = cv.FONT_HERSHEY_SIMPLEX
img = cv.putText(img, "OpenCV", (155, 100), font, 2.5, (0, 255, 0), 10, cv.LINE_AA)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()