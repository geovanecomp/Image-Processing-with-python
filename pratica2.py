import cv2
import numpy as np

# This file is about intensity transformation in a image.
# I will use three functions for that, negative to show a negative imagem,
# e logarithmic and exponential to increase or decrease the constrast.


img = cv2.imread("pout.tif", 0)
#img = cv2.imread("negative.jpeg") #Colorful Image
cv2.imshow("Image", img)
#cv2.waitKey(0)

def negative(r, L):
    return L - 1 - r

def logarithmic(r, c):
    return c*np.log(1+r)

def exponential(r, c, gama):
    return c*r**gama

def transformation(image):
    lines, cols = image.shape #get the quantity of lines and columns of the image
    #s = np.zeros((lines, cols), dtype=np.int) #Create a matrix of zeros in the same dimension of the passed image by parameter -> FAIL
    s = image
    L = 255 - 1
    c = 1
    gama = 0.8

    for i, row in enumerate(image):
        for j, col in enumerate(row):
            r = image[i][j]
            s[i][j] = negative(r, L)
            #s[i][j] = logarithmic(r, c)
            #s[i][j] = exponential(r, c, gama) #lambda is a reserved word in python


    return s

def colorfulTransformation(image):
    lines, cols, colors = image.shape #get the quantity of lines, columns and colors of the image
    #s = np.zeros((lines, cols, colors), dtype=np.int) #Create a matrix of zeros in the same dimension of the passed image by parameter -> FAIL
    s = image
    L = 65536 #16 bits image
    c = 1
    gama = 0.7

    for i, row in enumerate(image):
        for j, col in enumerate(row):
            for k, cor in enumerate(col):
                r = image[i][j][k]
                s[i][j][k] = negative(r, L)
                #s[i][j][k] = logarithmic(r, c)
                #s[i][j][k] = exponential(r, c, gama) #lambda is a reserved word in python

    return s

img2 = transformation(img)
cv2.imshow("Transformed Image", img)
cv2.waitKey(0)

print img
