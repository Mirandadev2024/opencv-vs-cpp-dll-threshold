import numpy as np
import time
import cv2 as cv

# lê a imagem
img = cv.imread("sunflower.jpg")

# converte para escala de cinza
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cópia para teste
img_test = img_gray.copy()

# mede o tempo
start = time.perf_counter()

_, out = cv.threshold(img_test, 130, 255, cv.THRESH_BINARY)

end = time.perf_counter()

print(f"OpenCV threshold: {(end - start)*1000:.3f} ms")

# mostra resultado
cv.imshow("resultado_opencv", out)

# salva imagem
cv.imwrite("sunflower_threshold_opencv.png", out)

cv.waitKey(0)
cv.destroyAllWindows()