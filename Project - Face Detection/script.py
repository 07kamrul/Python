import cv2

detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imp_img = cv2.VideoCapture("kamrul.jpeg")

res, img = imp_img.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = detect.detectMultiScale(gray,1.3,5)

cv2.imshow("Kamrul Hasan",img)

cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()
