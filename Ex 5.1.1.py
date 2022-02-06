import cv2
import numpy as np

image = cv2.imread('./image/sooyeon.png', cv2.IMREAD_COLOR)
if image is None :
    raise Exception("영상 파일 읽기 오류")

up_down = cv2.flip(image, 0)
left_right = cv2.flip(image,1)
up_down_left_right = cv2.flip(image, -1)
repeat = cv2.repeat(image, 2,4)
transpose = cv2.transpose(image)

titles = ['image', 'up_down', 'left_right', 'up_down_left_right', 'repeat', 'transpose']
for title in titles:
    cv2.imshow(title, eval(title))


cv2.waitKey(0)

