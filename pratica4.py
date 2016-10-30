# -*- coding: UTF-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

#To not abbreviate big matrices
np.set_printoptions(threshold='nan')

#0º step: Get the images and change the type
originalImage = cv2.imread('Cameraman.tif', 0)
originalImage = np.float32(originalImage)
M, N = np.shape(originalImage) #Number of lines and columns

#1º step: Get the filling parameters--------------------------------------------
M, N = np.shape(originalImage)
P = 2 * M
Q = 2 * N
distance = np.zeros((P,Q), dtype=np.float32)
H1 = np.zeros((P,Q), dtype=np.float32)
H2 = np.zeros((P,Q), dtype=np.float32)
filteredDft1 = np.zeros((P,Q), dtype=np.float32)
filteredDft2 = np.zeros((P,Q), dtype=np.float32)
D01 = 50
D02 = 50


#2º step: Building an image with the length of P and Q--------------------------
transformedImage = np.zeros((P,Q), dtype=np.float32)

for i in range(M):
    for j in range(N):
        transformedImage[i][j] = originalImage[i][j]

#3º step: Centering the Image---------------------------------------------------
#To move the information in the corners to the center in the frequency domain
def centeringImage(image):
    P, Q = np.shape(image)
    for i in range(P):
        for j in range(Q):
            image[i][j] = image[i][j] * (-1)**(i+j)
    return image

transformedImage = centeringImage(transformedImage)

#4º step: FFT calculation-------------------------------------------------------
dft1 = np.fft.fft2(transformedImage)
dft2 = np.fft.fft2(transformedImage)
#dft_shift = np.fft.fftshift(dft) #(another way) To move the information in the corners to the center in the frequency domain
#5º step: Apply the filter H: H(i,j)F(i,j)--------------------------------------

#Distance calculation to create the filters
for i in range(P):
    for j in range(Q):
        distance[i][j] = math.sqrt( (i - P/2)**2 + (j - Q/2)**2 )

#Creating the filters and applying then
for i in range(P):
    for j in range(Q):
        if distance[i][j] < D01:
            H1[i][j] = 1

        if distance[i][j] > D02:
            H2[i][j] = 1

        filteredDft1[i][j] =  H1[i][j]*dft1[i][j]
        filteredDft2[i][j] =  H2[i][j]*dft2[i][j]
#6º step: Applying the inverse transform----------------------------------------

img_back1 = np.fft.ifft2(filteredDft1)
img_back1 = centeringImage(img_back1)
transformedImage1 = np.zeros((M,N), dtype=np.float32)

img_back2 = np.fft.ifft2(filteredDft2)
img_back2 = centeringImage(img_back2)
transformedImage2 = np.zeros((M,N), dtype=np.float32)
