import numpy as np
import cv2

image = np.ones((200, 300), np.float)
cv2.namedWindow('Keyboard Event')
cv2.imshow('Keyboard Event', image)

# a 를 누르면 key = 33 이다.
# switch_case[33]
switch_case = {ord('a'): 'a 입력하셨습니다.',
               ord('b'): 'b 입력하셨습니다.',
               ord('A'): "A 입력하셨습니다.",
               2424832 : "왼쪽키"
               }

while True:
    key = cv2.waitKeyEx(10000)
    if key == 27:  # ESC 를 누르면
        break
    # print(key)
    try:
        result = switch_case[key]

    except KeyError:
        result = -1
    print(result)

cv2.destroyAllWindows()
