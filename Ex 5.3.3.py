import numpy as np
import cv2
x = np.array([1,2,3], np.float32)
y = np.array([2,5,7]).astype("float32")
# 1. cv2.magnitude
magnitude = cv2.magnitude(x,y)
print('magnitude :',np.ravel(magnitude))
# 2. cv2.phase
angle = cv2.phase(x,y)
print('angle :', np.ravel(angle))
# 3. cv2.cartToPolar
mag, ang = cv2.cartToPolar(x,y)
print(np.ravel(mag))
print(np.ravel(ang))
# 4. cv2.polarToCart
x_value, y_value = cv2.polarToCart(mag,ang)
print(x_value.flatten())
