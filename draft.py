# -*- coding:UTF-8 -*-
import numpy as np
import cv2
import timeit
import time
import matplotlib.pyplot as plt

np.set_printoptions(threshold='nan')

# load the games image
#timeit.Timer('for i in xrange(10): oct(i)', 'gc.enable()').timeit()
tempoInicial = time.time()
tempoClock = time.clock()
print 'The time is:', time.ctime()
img = cv2.imread("pout.tif")
#row, col = img.shape
cv2.imshow("Imagem teste",img)
#cv2.waitKey(0)

#PLOT USANDO O PLOTLIB
#plt.hist(img.ravel(),256,[0,256])


#PLOT USANDO O OPENCV (MAIS EFICIENTE QUE O PLOTLIB)
#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) # SINTAXE
#histr = cv2.calcHist([img],[0],None,[256],[0,256])
#plt.plot(histr)
#plt.show()

tempoPassado = time.time() - tempoInicial

print 'Duracao:', tempoPassado

x = len(img)
y = len(img[0])

#escreverImagem('matrizImagem', img)

posXmax, posYmax = encontrarPosMaiorElemento(img)
maiorElem =  img[posXmax][posYmax]

posXmin, posYmin = encontrarPosMenorElemento(img)
menorElem =  img[posXmin][posYmin]

#HISTOGRAMA
#histr = cv2.calcHist([img],[0],None,[256],[0,256])
#plt.plot(histr)
#plt.show()

print posXmax, posYmax, maiorElem, '\n',posXmin, posYmin, menorElem
#img2 = binarizarImagem(img, 100)
#cv2.imshow("Imagem 50", img)
#cv2.waitKey(0)
#Escrita e leitura em arquivo
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.show()

#arqImg.close()

#print img
