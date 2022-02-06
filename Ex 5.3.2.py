import numpy as np
import cv2

v1 = np.array([1,2,3], np.float32)
v1_exp = cv2.exp(v1)
v1_log = cv2.log(v1)
print(v1.shape)
print()
print(v1_exp)
print(v1_exp.shape)
print()
print(v1_log.shape)

print()
print(v1_log.T)
print(np.ravel(v1_log))
