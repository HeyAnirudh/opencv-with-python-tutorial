import cv2 as cv

cap = cv.VideoCapture(0)
print(cap.isOpened())

print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 3000)
cap.set(4, 2000)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()

    cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()