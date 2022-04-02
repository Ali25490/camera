import cv2

cam = cv2.VideoCapture(0)
while True:
    ret, img = cam.read()
    cv2.imshow('camera', img)
    if cv2.waitKey(10) == 27:
        break
cam.release()
cv2.destroyAllWindows()
