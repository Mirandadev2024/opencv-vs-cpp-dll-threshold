import numpy as np
import time
import cv2 as cv

# reads image
img = cv.imread("sunflower.jpg")

# converts to gray scale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# assures contiguous memory
img_gray = np.ascontiguousarray(img_gray)

# test copy (also contiguous)
img_test = np.ascontiguousarray(img_gray.copy())

# time measuring
start = time.perf_counter()

_, out = cv.threshold(img_test, 130, 255, cv.THRESH_BINARY)

end = time.perf_counter()

print(f"OpenCV threshold: {(end - start)*1000:.3f} ms")

# shows result
cv.imshow("result_opencv", out)

# save image
cv.imwrite("sunflower_threshold_opencv.png", out)

cv.waitKey(0)
cv.destroyAllWindows()