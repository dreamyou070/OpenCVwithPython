import numpy as np
import cv2

image = np.zeros((200,400), np.uint8)
image[:] = 200

title1, title2 = 'Position1', 'size changeable'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.moveWindow(title1, 0,0)
cv2.imshow(title1, image)

cv2.namedWindow(title2, cv2.WINDOW_NORMAL)
cv2.moveWindow(title2, 0,200)
cv2.waitKey(0)
cv2.destroyAllWindows()