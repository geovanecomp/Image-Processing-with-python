# -*- coding:UTF-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

#Para nao 'abreviar' matrizes grandes
np.set_printoptions(threshold='nan')

#Função para escrever em um arquivo a matriz / imagem para melhor visualizacao
def escreverImagem(arquivo, imagem):
    arqImg = open(arquivo, 'w')

    for row in img:
        for col in row:
            arqImg.write(str(col)+"  ")

        arqImg.write('\n\n')

    arqImg.close()

def encontrarPosMaiorElemento(matriz):

    maiorElem = 0
    posX = 0
    posY = 0
    for i, row in enumerate(matriz):
        for j, col in enumerate(row):
            if maiorElem < matriz[i][j]:
                maiorElem = matriz[i][j]
                posX = i
                posY = j
    return posX, posY

def encontrarPosMenorElemento(matriz):

    menorElem = 255
    posX = 0
    posY = 0
    for i, row in enumerate(matriz):
        for j, col in enumerate(row):
            if menorElem > matriz[i][j]:
                menorElem = matriz[i][j]
                posX = i
                posY = j
    return posX, posY

def binarizarImagem(imagem, limitador):
    for i, row in enumerate(imagem):
        for j, col in enumerate(row):

            if imagem[i][j] < limitador:
                imagem[i][j] = 0
            else:
                imagem[i][j] = 255
    return imagem

#Para inverter tal imagem, crio outra de zeros para otimizacao de mesmo tamanho
#da original. Feito isso eu crio dois indices, um comecando normal e outro de
#baixo para cima (tamX - i) para popular a imagem invertida.
#Talvez fosse melhor usar a matriz de rotacao.
def inverterImagem(imagem):

    tamX = len(imagem)
    tamY = len(imagem[0])
    imagemInvertida = np.zeros((tamX, tamY))

    #Vetores comecam de zero e vao ate n-1, por isso da seguinte correcao
    tamX -= 1
    tamY -= 1
    for i, row in enumerate(imagem):
        for j, col in enumerate(row):
            posImgInvertidaX = tamX - i
            posImgInvertidaY = tamY - j
            imagemInvertida[posImgInvertidaX][posImgInvertidaY] = imagem[i][j]

    return imagemInvertida

#------------------------------------------------------------------------------

#Item 1 - CARREGAR E EXIBIR UMA IMAGEM
#img = cv2.imread("pout.tif", 0) #Lê a imagem e a atribui como matriz a img, 0 para escala de cinza, > 0 para rgb
#cv2.imshow("Imagem 1", img) #Exibe a imagem com o tipo passado
#cv2.waitKey(0)              #Exibe a imagem ate que a tecla zero for passada


#-------------------------------------------------------------------------------

#Item 2 - ENCONTRAR POSICAO DO MAIOR E MENOR ELEMENTO
#posXmax = 0
#posYmax = 0

#posXmin = 0
#posYmin = 0
#posXmax, posYmax = encontrarPosMaiorElemento(img)
#maiorElem =  img[posXmax][posYmax]

#posXmin, posYmin = encontrarPosMenorElemento(img)
#menorElem =  img[posXmin][posYmin]

#print posXmax, posYmax, maiorElem, '\n',posXmin, posYmin, menorElem

#-------------------------------------------------------------------------------

#Item 3 - HISTOGRAMA
#histr = cv2.calcHist([img],[0],None,[256],[0,256])
#plt.plot(histr)
#plt.show()

#-------------------------------------------------------------------------------

#Item 3 - BINARIZAR A IMAGEM EM FUNÇÃO DOS LIMITADORES PASSADOS
#img2 = cv2.imread("pout.tif", 0)
#img3 = cv2.imread("pout.tif", 0)
#img4 = cv2.imread("pout.tif", 0)

#img2 = binarizarImagem(img2, 50)
#comp2 = np.hstack((img,img2)) #Colocando duas imagens lado a lado

#plt.imshow(comp2, cmap = 'gray', interpolation = 'bicubic')
#plt.show()

#img3 = binarizarImagem(img3, 120)
#comp3 = np.hstack((img,img3))
#cv2.imwrite('img3.png',comp3) #Como esta imagem eh melhor para comparacao, a salvei no computador
#plt.imshow(comp3, cmap = 'gray', interpolation = 'bicubic')
#plt.show()

#img4 = binarizarImagem(img4, 200)
#comp4 = np.hstack((img,img4))
#plt.imshow(comp4, cmap = 'gray', interpolation = 'bicubic')
#plt.show()

#-------------------------------------------------------------------------------

#item 4 - INVERTER A IMAGEM
imagem = cv2.imread("pout.tif", 0)
imagemInvertida = inverterImagem(imagem)
compInvertida = np.hstack((imagem,imagemInvertida))
plt.imshow(compInvertida, cmap = 'gray')
plt.show()
