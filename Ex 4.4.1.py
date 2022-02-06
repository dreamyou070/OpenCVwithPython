import cv2


def print_matInfo(name, image):
    if image.dtype == 'uint8':
        mat_type = "CV_8U"
    elif image.dtype == 'int8':
        mat_type = "CV_8S"
    elif image.dtype == 'uint16' :
        mat_type = "CV_16U"
    elif image.dtype == 'int16' :
        mat_type = "CV_16S"
    elif image.dtype == 'float32' :
        mat_type = "CV_32F"
    elif image.dtype == 'float64' :
        mat_type = 'CV_64F'
    nchannel = 3 if image.ndim == 3 else 1

    print('%12s : '%(name))

title1, title2 = 'gray2gray', 'gray2color'
gray2gray  = cv2.imread('image/color_map.png', cv2.IMREAD_GRAYSCALE)
gray2color = cv2.imread('image/color_map.png', cv2.IMREAD_COLOR)

if gray2gray is None or gray2color is None :
    raise Exception('영상 파일 읽기 에러')






