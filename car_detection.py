# import modules
import cv2

# read image
img_read_from_system = 'car.jpg'

# read harr cascade file
haar_car_data = 'cars.xml'

# rad xcml file with cv2
car_data = cv2.CascadeClassifier(haar_car_data)

# read the inage by opencv
img = cv2.imread(img_read_from_system)

# convert the image to black and white
img_black_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# read cordinates
car = car_data.detectMultiScale(img_black_white)

# print coordinates
print(car)

# loop through coordinates
for (x, y, w, h) in car:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 5)

#show image
cv2.imshow('car and predestian detection', img)

# wait key
cv2.waitKey(0)


# unit testing code
print("code complete")