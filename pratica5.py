# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#To not abbreviate big matrices
np.set_printoptions(threshold='nan')

#1º Step: Get the images and define auxiliary matrices--------------------------
originalImage = cv2.imread('pepper.jpg', 3)

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
def medianOfMask (image, x, y, z, dimension=3):

    #A mask must be square
    totalElements = dimension * dimension

    vector = np.zeros(totalElements, dtype=np.float32)
    position = 0

    #Transforming a matrix in an array
    for i in range(x, x+dimension):
        for j in range(y, y+dimension):
            vector[position] = image[i][j][z]
            position += 1

    #Sorting the array
    ordenedVector = np.sort(vector)

    #The median is located in the half of the array
    middlePosition = np.rint(totalElements/2)

    return ordenedVector[middlePosition]

#Main function
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
                value = medianOfMask(image, x, y, z, dimensionMask)

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
