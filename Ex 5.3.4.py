import numpy as np
import cv2
width = 300
height = 300
radius =int(width / 3)
center_x = int(width/2)
center_y = int(height/2)

image1 = np.zeros((height, width), np.uint8)
image2 = image1.copy()
cv2.circle(image1,(center_x,center_y), radius, 255, -1)
cv2.imshow('image1', image1)

cv2.rectangle(image2, (0,0,center_x,center_y), 255,-1)
cv2.imshow('image2', image2)

image3 = cv2.bitwise_or(image1, image2)
cv2.imshow('image3',image3)

image4 = cv2.bitwise_and(image1, image2)
cv2.imshow('image4',image4)

image5 = cv2.bitwise_xor(image1, image2)
cv2.imshow('image5',image5)

image6 = cv2.bitwise_not(image1)
cv2.imshow('image6',image6)

cv2.waitKey(0)



