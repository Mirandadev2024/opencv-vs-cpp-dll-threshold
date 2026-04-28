import cv2 as cv
import numpy as np
import ctypes
import time
from ctypes import c_uint8, c_int, POINTER

# loads DLL
mylib = ctypes.CDLL("./opencvdll.dll")

# read image
img = cv.imread("sunflower.jpg")

# converte para escala de cinza
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# assures contiguous memory
img_gray = np.ascontiguousarray(img_gray)

# DLL specifications
mylib.threshold_custom.argtypes = [
    POINTER(c_uint8),  # unsigned char* img
    c_int,             # int rows
    c_int,             # int cols
    c_uint8            # unsigned char t
]
mylib.threshold_custom.restype = None  # void

start = time.perf_counter()

# calls C++ function
mylib.threshold_custom(
    img_gray.ctypes.data_as(POINTER(c_uint8)),
    img_gray.shape[0],
    img_gray.shape[1],
    130
)

end = time.perf_counter()

print(f"Time: {(end-start)*1000:.3f}ms")

# shows result
cv.imshow("result", img_gray)

cv.imwrite("sunflower_threshold.png", img_gray)

cv.waitKey(0)
cv.destroyAllWindows()
