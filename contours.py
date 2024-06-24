import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
# cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('Threshold', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours', blank)

cv.waitKey(0)
