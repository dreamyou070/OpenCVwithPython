# 직선 그리기
import numpy as np
import cv2

blue, green, red = (255,0,0), (0,255,0),(0,0,255)
image = np.zeros((400,600,3), np.uint8)
image[:] = (255,255,255)

roi = (50,200,200,100)
cv2.rectangle(image, roi, red, 3, cv2.LINE_4)
cv2.imshow('image', image)
cv2.waitKey(0)