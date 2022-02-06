import cv2
from utils import put_string

capture = cv2.VideoCapture(0)
if not capture.isOpened():
    raise Exception("카메라 연결 안됨")

print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE)) # -6 값이다.
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS)) # 밝기의 값이 64이다.

while True:
    ret, frame = capture.read()
    if not ret:
        break
    if cv2.waitKey(30) >= 0:
        break

    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    print(exposure)
    put_string(frame, 'EXPOS: ', (100, 300), exposure)
    title = "View Frame from Camera"
    cv2.imshow(title, frame)
capture.release()
