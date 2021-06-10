from cv2 import cv2 as cv
import math
# cap = cv.VideoCapture(0)

# while True:
#     _, frame = cap.read()
class EyeDetector:
    def __init__(self,no_of_eye:int):
        self.haar_cascade = cv.CascadeClassifier('eye.xml')
        self.no_of_eye = no_of_eye
    def find_eye(self,img):
        if self.no_of_eye == 1:
            faces_rect = faces_rect[
        for x, y, w, h in faces_rect:
            self.x1,self.y1 = x,y
            self.x2,self.y2 = x+w,h+y
            self.cx, self.cy = (x1 + x2) // 2, (y1 + y2) // 2
            cv.circle(frame,(cx,cy),3,(0,0,255),cv.FILLED)
            cv.circle(frame,(x1,y1),3,(0,225,0),cv.FILLED)
            cv.circle(frame, (x2, y2), 3, (0, 225, 0), cv.FILLED)
            cv.circle(frame, (x1, y2), 3, (0, 225, 0), cv.FILLED)
            cv.circle(frame, (x1, y2), 3, (0, 225, 0), cv.FILLED)
            cv.circle(frame, (x2, y1), 3, (0, 225, 0), cv.FILLED
    def findPosition(

   
cap.release()
cv.destroyAllWindows()
