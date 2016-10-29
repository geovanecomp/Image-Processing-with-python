# -*- coding: UTF-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

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
dft = cv2.dft(transformedImage, flags = cv2.DFT_COMPLEX_OUTPUT)
#dft_shift = np.fft.fftshift(dft) #(another way) To move the information in the corners to the center in the frequency domain
magnitude_spectrum = 20*np.log(cv2.magnitude(dft[:,:,0],dft[:,:,1]))

originalImage = np.uint8(originalImage)
plt.subplot(121),plt.imshow(originalImage, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# cv2.imshow("1º step", transformedImage)
# cv2.waitKey(0)
