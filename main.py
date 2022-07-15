import cv2 #opencv를 활용하여 얼굴인식 구현

# xml 파일 지정
face_cascade = 'haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(face_cascade) # 얼굴 인식 xml


img = cv2.imread('sample.png') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
face_list = cascade.detectMultiScale(gray, minSize = (50,50)) # 얼굴검출

for (x, y, w, h) in face_list:
    color = (102, 102, 204)  
    pen_w = 2 
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w)     
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
cv2.imwrite('sample_01.jpg', img) 
cv2.waitKey(0)

