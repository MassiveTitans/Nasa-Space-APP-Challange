import pyfirmata
import led_matrix
from cv2 import cv2 as cv
import speech_recognition as sr


x = [[1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1]]

fine = [[1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1]]


cap = cv.VideoCapture(0)

net = cv.dnn.readNet('yolov4-tiny-custom_best.weights', 'yolov4-tiny-custom.cfg')
model = cv.dnn_DetectionModel(net)
model.setInputParams(size = (320 , 320) , scale= 1/255)

port = pyfirmata.Arduino('COM6')
led = led_matrix.LedMatrix(board=port)
led.setup()


while True:
    _ , frame = cap.read()

    # biometrik tekshiruv
    (classids , scores , boxes) = model.detect(frame)
    for _ in classids:
        if _ ==0:
            try:
                recog = sr.Recognizer()
                with sr.Microphone(2) as mic:
                    recog.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recog.listen(mic)
                    text = recog.recognize_google(audio, language='en-EN')
                    aa = text.lower()
                    if aa == 'open':
                        led.draw_matrix(fine)
                    if aa == 'close' or aa == 'glass':
                        led.draw_matrix(x)
            except:
                pass