'''
Developer : Hardware and Software (A.I.) Engineer
Yaxshiliqov Javlon Qaxramon o'g'li
+99894 463 70 30
This project for NASA Hackathon (01.10.2022)
Thanks for visiting!
'''

import led_matrix
import cv2.cv2 as cv
import pyfirmata
import index
import mediapipe as mp





# AI model (custom biometrik model 'Yaxshiliqov Javlon')
net = cv.dnn.readNet('yolov4-tiny-custom_best.weights', 'yolov4-tiny-custom.cfg')
model = cv.dnn_DetectionModel(net)
model.setInputParams(size = (320 , 320) , scale= 1/255)




# connector for Arduino
port = pyfirmata.Arduino('COM6')
led = index.Led(port = port)


# mediapipe for AI
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


# video capture from web-Camera or PC
cap = cv.VideoCapture(0)


# Qo'shimcha parametrlar
def Masofa(x1, y1 , x2 , y2):
    aa = int(((x1-x2)**2 + (y1 -y2)**2)**(1/2))
    return aa


cordinata_1_x , cordinata_1_y = 0 , 0
cordinata_2_x , cordinata_2_y = 0 , 0
uzunlik = []
x1 , y1 = 0 , 0
x2 , y2 = 0 , 0


while True:
    _ ,  frame  = cap.read()
    imageRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    #obyektni aniqlash
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:  # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:
                    cordinata_1_x = cx
                    cordinata_1_y = cy
                if id == 4:
                    cordinata_2_x = cx
                    cordinata_2_y = cy
                if id == 5:
                    x1 = cx
                    y1 = cy
                if id == 0:
                    x2 = cx
                    y2 = cy

                aa = Masofa(x1 , y1 , x2 , y2 )
                bb = Masofa(cordinata_1_x , cordinata_1_y , cordinata_2_x , cordinata_2_y)
                if bb ==0:
                    bb = 1
                led.led(aa , bb)
                led.qizil_led(aa , bb)
                cv.line(frame, (cordinata_1_x, cordinata_1_y), (cordinata_2_x, cordinata_2_y), (255, 0, 0), 3)


            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

    cv.imshow('video' , frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()