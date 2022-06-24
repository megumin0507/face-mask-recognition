import cv2


casc_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc_path)
maskCascade = cv2.CascadeClassifier("haar_mask.xml")
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, img = cap.read()
    if ret:
        img = cv2.resize(img, (300, 225))
        masks = maskCascade.detectMultiScale(img, minSize = (30, 30), scaleFactor=1.1, minNeighbors=6)
        faces = faceCascade.detectMultiScale(img, minSize = (30, 30), scaleFactor=1.1, minNeighbors=4, flags = cv2.CASCADE_SCALE_IMAGE)
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.imshow('Frame', img)
        elif len(masks) > 0:
            for (x, y, w, h) in masks:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow('Frame', img)    
        else:
            cv2.imshow('Frame', img)
        k = cv2.waitKey(100)
        if k == ord("q") or k == ord('Q'):
            cv2.imwrite('catch.jpg', img)
            break
        print(len(faces), len(masks))

cap.release()
cv2.destroyAllWindows()
