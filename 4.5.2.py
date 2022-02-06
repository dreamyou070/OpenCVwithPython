import cv2
import numpy as np

ch0 = np.zeros((2,4), np.uint8) + 10
ch1 = np.ones((2,4), np.uint8) * 20
ch2 = np.full((2,4),30,  np.uint8)

list_bgr = [ch0,ch1,ch2]
merge_bgr = cv2.merge(list_bgr)
split_bgr = cv2.split(merge_bgr)

print(list_bgr)
print()
print(merge_bgr)