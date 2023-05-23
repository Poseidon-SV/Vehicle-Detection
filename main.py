import cv2 #image acquisition if
import imutils #resize the frame

cascade_src = 'cars.xml' #initiialize alg file name

car_cascade = cv2.CascadeClassifier(cascade_src) #loading the model
cam=cv2.VideoCapture(0) #initializing the camera

while True: #inf. loop

    detected = 0
    _,img=cam.read() #reading frame from camera
    img=imutils.resize(img,width=600) #resize to 300
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #color to Grayscale
    cars = car_cascade.detectMultiScale (gray, 1.1, 1) #coordinates of vehicle
    for (x,y,w,h) in cars:
        cv2.rectangle (img, (x,y), (x+w,y+h), (0,0,255) ,2)

    cv2.imshow("Frame", img)
    b=str(len(cars))
    a= int(b)
    detected=a
    n=detected
    print("-----------------------------------------------")
    print ("Vehicale Detected: %d "%(n))

    if n>=2:
        print ("Traffic")
    else:
        print ("No Traffic")
    if cv2.waitKey(33) == 27:
        break

cam. release()
cv2.destroyAllWindows()
