import cv2 as cv

img = cv.imread("download (2).jpeg",-1)


cv.imshow("image",img)
grey=cv.cvtColor()
f=cv.waitKey()
if f == 27:
    cv.destroyAllWindows()
elif f == ord("f"):
    cv.imwrite("new img ",grey)

