import cv2 as cv
import numpy as np
img = cv.imread('C:/Users/User 2/Desktop/Tyson.jpg')


#Translation

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

        # -x is left
        # x is right
        # -y is up
        # y is down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)
cv.waitKey(0)


#Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)
cv.waitKey(0)



#Flip
flipped = cv.flip(img, -1)  #0 is over x axis, 1 is over y axis, -1 is both axes
cv.imshow('Flipped', flipped)
cv.waitKey(0)