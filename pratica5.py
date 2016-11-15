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
