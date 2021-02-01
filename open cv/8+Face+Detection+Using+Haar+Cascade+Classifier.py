import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv.imread("Team-ManU.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face_detect = face_cascade.detectMultiScale(gray_img, 1.1, 3)

for (x, y, w, h) in face_detect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=5)

cv.imshow("Image", img)
cv.waitKey(0)