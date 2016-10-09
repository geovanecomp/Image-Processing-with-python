import cv2
import numpy as np


img = cv2.imread("pout.tif", 0)
#img = cv2.imread("negativa.jpeg") #Imagem colorida
cv2.imshow("Imagem", img)
#cv2.waitKey(0)

def quantificarPixels(imagem, qtdBits):
    s = np.zeros((2**qtdBits), dtype=np.int)

    print len(s)

quantificarPixels(img, 8)
