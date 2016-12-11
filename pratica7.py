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

#4º step: Use a % from dct and calculate the inverse DCT------------------------
def getPercentOfDct(image, percent):
    newImage = np.zeros(image.shape, dtype=np.float32)
    M, N = image.shape
    M2 = int(M * (percent/100.0))
    N2 = int(N * (percent/100.0))
    print "Nova dimensao", M2, N2
    for i in range(M2):
        for j in range(N2):
            newImage[i][j] = image[i][j]

    return newImage

def iDct(dctImage, m, n):
    value = 0.0

    for p in range(M):
        for q in range(N):
            value += alphaP(p)*alphaQ(q) * dctImage[p][q] * math.cos( (math.pi * (2*m + 1) * p) / (2*M) ) * math.cos( (math.pi * (2*n + 1) * q) / (2*N) )

    return value

def iDctCalculation (dctImage):
    iDctImage = np.zeros(dctImage.shape, dtype=np.float32)

    print 'Iniciando da transformada inversa:'
    for m in range(M):
        for n in range(N):
            iDctImage[m][n] = iDct(dctImage, m, n)

    print iDctImage
    return iDctImage


#5º Step: Calling the functions-----------------------------------------------

transformedImageDCT = dctCalculation(originalImage)
partOfDct = getPercentOfDct(transformedImageDCT, 30)
transformedImageIDCT = iDctCalculation(partOfDct)

#6º step: Showing the results---------------------------------------------------

#Showing the images
plt.figure(1)
plt.subplot(141),plt.imshow(originalImage, cmap = 'gray')
plt.title('Imagem de entrada '), plt.xticks([]), plt.yticks([])
plt.subplot(142),plt.imshow(transformedImageDCT, cmap = 'gray')
plt.title('DCT'), plt.xticks([]), plt.yticks([])
plt.subplot(143),plt.imshow(partOfDct, cmap = 'gray')
plt.title('% da DCT'), plt.xticks([]), plt.yticks([])
plt.subplot(144),plt.imshow(transformedImageIDCT, cmap = 'gray')
plt.title('IDCT'), plt.xticks([]), plt.yticks([])
plt.show()
