import cv2 as cv

img = cv.imread('Photos/cat.jpg')

# cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
# cv.imshow('Blur', canny)

dileted = cv.dilate(canny, (7, 7), iterations=1)
# cv.imshow('Blur', dileted)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Blur', resized)

cropped = img[50:200, 200:400]
cv.imshow('Blur', cropped)

cv.waitKey(0)
