import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

img = cv.imread("Ronaldo-1.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face_detect = face_cascade.detectMultiScale(gray_img, 1.1, 4)
eye_detect = eye_cascade.detectMultiScale(gray_img)

for (x, y, w, h) in face_detect:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=3)

    for (ex, ey, ew, eh) in eye_detect:
        cv.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), thickness=3)

cv.imshow("Image", img)
cv.waitKey(0)