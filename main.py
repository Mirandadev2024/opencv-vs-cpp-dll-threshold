import cv2 as cv
import numpy as np
import ctypes
import time
from ctypes import c_uint8, c_int, POINTER

# carrega a DLL
mylib = ctypes.CDLL("./opencvdll.dll")

# lê a imagem
img = cv.imread("sunflower.jpg")

# converte para escala de cinza
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# garante memória contígua
img_gray = np.ascontiguousarray(img_gray)

# especificação da função da DLL
mylib.threshold_custom.argtypes = [
    POINTER(c_uint8),  # unsigned char* img
    c_int,             # int rows
    c_int,             # int cols
    c_uint8            # unsigned char t
]
mylib.threshold_custom.restype = None  # void

start = time.perf_counter()

# chama a função C++
mylib.threshold_custom(
    img_gray.ctypes.data_as(POINTER(c_uint8)),
    img_gray.shape[0],
    img_gray.shape[1],
    130
)

end = time.perf_counter()

print(f"Tempo: {(end-start)*1000:.3f}ms")

# mostra o resultado
cv.imshow("resultado", img_gray)

cv.imwrite("sunflower_threshold.png", img_gray)

cv.waitKey(0)
cv.destroyAllWindows()
