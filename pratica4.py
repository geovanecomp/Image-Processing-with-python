# -*- coding: UTF-8 -*-
import numpy as np
import cv2

#0º step: Get the images and change the type
originalImage = cv2.imread('lua.tif', 0)
originalImage = np.float32(originalImage)
M, N = np.shape(originalImage) #Number of lines and columns

#1º step: Get the filling parameters--------------------------------------------
M, N = np.shape(originalImage)
P = 2 * M
Q = 2 * N

#2º step: Building an image with the length of P and Q--------------------------
transformedImage = np.zeros((P,Q), dtype=np.float32)

for i in range(M):
    for j in range(N):
        transformedImage[i][j] = originalImage[i][j]
