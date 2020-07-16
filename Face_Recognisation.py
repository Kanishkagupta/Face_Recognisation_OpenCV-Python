import cv2
faceCascade=cv2.CascadeClassifier("C:/Users/AMAN/Desktop/data/haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    if success:
        imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(imgGray,1.1,4)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
            cv2.imshow("Face Detect",img)
            cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()

