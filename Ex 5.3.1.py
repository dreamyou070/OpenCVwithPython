import numpy as np
import cv2

m1 = np.full((1,2), 10, np.uint8)
m2 = np.full((1,2), 50, np.uint8)
m_mask = np.zeros(m1.shape, np.uint8)
m_mask[:,1:] = 1


m_add1 = cv2.add(m1,m2)
m_add2 = cv2.add(m1,m2, mask=m_mask)
m_div1 = cv2.divide(m1,m2)
m1 = m1.astype(np.float32)

m2 = np.float32(m1)
print()
print(m2)