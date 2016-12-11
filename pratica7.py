# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time
import math

#To not abbreviate big matrices
np.set_printoptions(threshold='nan')

#This file is for compress an image

#1º Step: Get the images and define auxiliary matrices--------------------------
originalImageFull = cv2.imread('Cameraman.tif', 0)
originalImage = np.zeros((100,100), dtype=np.float32)


#To use only 100x100 elements in the matrix (faster)
infLimit = 100
supLimit = 200
contX = 0
contY = 0
for i in range(infLimit, supLimit):
    for j in range(infLimit, supLimit):
        originalImage[contX][contY] = originalImageFull[i][j]
        contY +=1
    contX += 1
    contY = 0

M, N = originalImage.shape

#Converting the image to make operations
originalImage = np.float32(originalImage)
transformedImageDCT = np.zeros(originalImage.shape, dtype=np.float32)
transformedImageIDCT = np.zeros(originalImage.shape, dtype=np.float32)

#2º Step: DCT and IDCT by opencv------------------------------------------------

# transformedImageDCT = cv2.dct(originalImage)
# transformedImageIDCT = cv2.idct(transformedImageDCT)

#2º step: DCT-------------------------------------------------------------------
def alphaP(p):
    if p == 0:
        return 1.0/math.sqrt(M)
    else:
        return math.sqrt(2.0/M)

def alphaQ(q):
    if q == 0:
        return 1.0/ math.sqrt(N)
    else:
        return math.sqrt(2.0/N)

def dct(image, p, q):
    value = 0.0

    for m in range(M):
        for n in range(N):
            value += image[m][n] * math.cos( (math.pi * (2*m + 1) * p) / (2*M) ) * math.cos( (math.pi * (2*n + 1) * q) / (2*N) )

    return value

def dctCalculation (image):
    dctImage = np.copy(image)

    for p in range(M):
        for q in range(N):
            dctImage[p][q] = alphaP(p)*alphaQ(q)*dct(image, p, q)

    return dctImage
