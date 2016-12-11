# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time

#To not abbreviate big matrices
np.set_printoptions(threshold='nan')


#This file is for calculate the Sobel masks

#1º Step: Get the images and define auxiliary matrices--------------------------
originalImage = cv2.imread('house.jpg', 0)
initialTime = time.time()
try:
    M, N, O = originalImage.shape
except:
    M, N = originalImage.shape
    O = 1
    originalImage = originalImage.reshape((M,N,O))
print 'Past time:', time.time() - initialTime
print originalImage.shape

#Converting the image to make operations
originalImage = np.float32(originalImage)

#2º Step: Define the auxiliary functions----------------------------------------

def addRows(matrix, quantity, position, values=0):
    for i in range(quantity):
        matrix = np.insert(matrix, position, values, axis=0)
    return matrix

def addColumns(matrix, quantity, position, values=0):
    for i in range(quantity):
        matrix = np.insert(matrix, position, values, axis=1)
    return matrix

def deleteRows(matrix, quantity, position):
    for i in range(quantity):
        position -= 1
        matrix = np.delete(matrix, position, axis=0)
    return matrix

def deleteColumns(matrix, quantity, position):
    for i in range(quantity):
        position -= 1
        matrix = np.delete(matrix, position, axis=1)
    return matrix

#3º step: Removing the noises---------------------------------------------------

#To remove the noises a lot of methods can be used, like average, median and others.
#Here I'm using the median with the default dimension = 3, but we could use others.
def averageMask (image, x, y, z, dimension=3):

    #A mask must be square
    totalElements = dimension * dimension

    vector = np.zeros(totalElements, dtype=np.float32)
    average = 0

    #Transforming a matrix in an array
    for i in range(x, x+dimension):
        for j in range(y, y+dimension):
            average += image[i][j][z]

    return average / totalElements

def removeNoise(image, dimensionMask=3):

    image = addRows(image, dimensionMask - 1, 0)
    image = addRows(image, dimensionMask - 1, len(image))

    image = addColumns(image, dimensionMask - 1, 0)
    image = addColumns(image, dimensionMask - 1, len(image[0]))

    g = np.zeros(image.shape, dtype=np.float32)

    value = 0

    lenX, lenY, lenZ = image.shape

    for x in range(lenX - (dimensionMask - 1)):
        for y in range(lenY - (dimensionMask - 1)):
            for z in range(lenZ):
                value = averageMask(image, x, y, z, dimensionMask)

                if value < 0:
                    value = 0

                if value > 255:
                    value = 255

                g[x][y][z] = value
                value = 0

    g = deleteRows(g, dimensionMask - 1, 0)
    g = deleteRows(g, dimensionMask - 1, len(g))

    g = deleteColumns(g, dimensionMask - 1, 0)
    g = deleteColumns(g, dimensionMask - 1, len(g[0]))

    return g



#3º step: Get the sobelMask---------------------------------------------------

def sobel(image, dimensionMask=3):
    image = removeNoise(image, dimensionMask)

    maskX = [[-1,-2,-1], [0,0,0], [1,2,1]]
    maskY = [[-1,0,1], [-2,0,2], [-1,0,1]]

    image = addRows(image, dimensionMask - 1, 0)
    image = addRows(image, dimensionMask - 1, len(image))

    image = addColumns(image, dimensionMask - 1, 0)
    image = addColumns(image, dimensionMask - 1, len(image[0]))

    sobelMaskX = np.zeros(image.shape, dtype=np.float32)
    sobelMaskY = np.zeros(image.shape, dtype=np.float32)
    sobelMask  = np.zeros(image.shape, dtype=np.float32)

    valueX = 0
    valueY = 0

    lenX, lenY, lenZ = image.shape

    for x in range(lenX - (dimensionMask - 1)):
        for y in range(lenY - (dimensionMask - 1)):
            for z in range(lenZ):
                for s in range(len(maskX)):
                    for t in range(len(maskX[0])):
                        valueX = maskX[s][t]*image[x+s][y+t] + valueX
                        valueY = maskY[s][t]*image[x+s][y+t] + valueY

                if valueX < 0:
                    valueX = 0

                if valueX > 255:
                    valueX = 255

                if valueY < 0:
                    valueY = 0

                if valueY > 255:
                    valueY = 255

                sobelMaskX[x][y][z] = valueX
                sobelMaskY[x][y][z] = valueY
                sobelMask[x][y][z] = sobelMaskX[x][y][z] + sobelMaskY[x][y][z]
                valueX = 0
                valueY = 0

    sobelMask = deleteRows(sobelMask, dimensionMask - 1, 0)
    sobelMask = deleteRows(sobelMask, dimensionMask - 1, len(sobelMask))

    sobelMask = deleteColumns(sobelMask, dimensionMask - 1, 0)
    sobelMask = deleteColumns(sobelMask, dimensionMask - 1, len(sobelMask[0]))

    return sobelMask

#4º step: Main function---------------------------------------------------------

def threshold(image, dimensionMask=3):

    sobelMask = sobel(image, dimensionMask)
    M,N,O = sobelMask.shape
    transformedImage = np.zeros(image.shape, dtype=np.float32)

    limiter = sobelMask.max()*0.13
    for x in range(M):
        for y in range(N):
            for z in range(O):
                if sobelMask[x][y][z] > limiter:
                    transformedImage[x][y][z] = 255


    return transformedImage


#5º step: Showing the results---------------------------------------------------
transformedImage = threshold(originalImage,5)
#Converting the images to unsigned int
originalImage = np.uint8(originalImage)
transformedImage = np.uint8(transformedImage)

#Showing the images
cv2.namedWindow('Imagem original vs 3x3 vs 5x5',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Imagem original vs 3x3 vs 5x5', 1200, 600)
imageComparison = np.hstack((originalImage, transformedImage))

cv2.imshow('Imagem original vs 3x3 vs 5x5', imageComparison)
cv2.imwrite('resultadoPratica6.jpg', imageComparison)
cv2.waitKey(0)
