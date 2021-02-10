# import module
import cv2
from random import randrange

# webcam
webcam = cv2.VideoCapture('car1.avi')

# trained data
car_data = cv2.CascadeClassifier('cars.xml')
count =0
while True:
    # read the frame from webcam
    successful_frame_read, frame = webcam.read()
    if successful_frame_read:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        print("frame read unsuccessful")
        break
    car_coordinates = car_data.detectMultiScale(gray_frame)
    for (x, y, w, h) in car_coordinates:
        print(car_coordinates)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 5)
        count += 1
    cv2.imshow("just watch ", frame)
    # wait key
    key = cv2.waitKey(1)
    if key==81 or key ==113:
        break

#unit testing code
print(count)
print('code complete')