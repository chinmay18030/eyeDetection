from cv2 import cv2 as cv
import math
cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier('C:/Users/My/Desktop/Ace Tech Academy/Data/XML/eye.xml')
    faces_rect: None = haar_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=30)

    for x, y, w, h in faces_rect:
        # c = w*h
        # if c > 1000:
        #     cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
        # lenght = math.hypot(x-(x+w),y-(y+h))
        # print(lenght)
        # cv.line(frame,(x,y),(x+w,h+y),(255,255,255),3)
        x1,y1 = x,y
        x2,y2 = x+w,h+y
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv.circle(frame,(cx,cy),3,(0,0,255),cv.FILLED)
        cv.circle(frame,(x1,y1),3,(0,225,0),cv.FILLED)
        cv.circle(frame, (x2, y2), 3, (0, 225, 0), cv.FILLED)
        cv.circle(frame, (x1, y2), 3, (0, 225, 0), cv.FILLED)
        cv.circle(frame, (x1, y2), 3, (0, 225, 0), cv.FILLED)
        cv.circle(frame, (x2, y1), 3, (0, 225, 0), cv.FILLED)


    cv.imshow("hello", frame)
    if cv.waitKey(1) & 0xFF == ord('c'):
        break
cap.release()
cv.destroyAllWindows()
