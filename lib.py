import numpy as np
import matplotlib.pyplot as mp
import os
from PIL import Image

####################################### LAB 1 #######################################

"""
0.2 - Crie uma função chamada imread que recebe um nome de arquivo e retorna a imagem
lida. O tipo da imagem retornada deve ser numpy.ndarray e o de seus pixels, uint8.
"""


def imread(filename):
    im = mp.imread(filename)
    if im.dtype == "float32":
        im = np.uint8(255 * im)
    if len(im.shape) >= 3 and im.shape[2] > 3:
        im = im[:, :, 0:3]
    return im


"""
0.3 - Crie uma função chamada imshow que recebe uma imagem como parâmetro e a exibe.
Se a imagem for em escala de cinza, exiba com colormap gray. Sempre usar interpolação
nearest para que os pixels apareçam como quadrados ao dar zoom ou exibir imagens
pequenas
"""


def imshow(im):
    plot = mp.imshow(im, cmap=mp.gray(), origin="upper")
    plot.set_interpolation('nearest')
    mp.show()


def aux_show(filename):
    imshow(imread(filename))

'''
a)aux_show("lena/lena_std.png")
b)aux_show("lena/lena_gray.png")
c)aux_show("lena/lena_25_eye.png")
'''

"""
1 - Crie uma função chamada nchannels que retorna o número de canais da imagem de
entrada.
"""


# Dúvida
def nchannels(filename):
    im = imread(filename)
    i = im.shape
    return i[2] if len(i) == 3 else 1 if len(i) == 2 else 0 

# print(nchannels("lena/lena_std.png"))
# print(nchannels("lena/lena_gray.png"))


"""
2 - Crie uma função chamada size que retorna um vetor onde a primeira posição é a largura
e a segunda é a altura em pixels da imagem de entrada.
"""


def size(filename):
    im = imread(filename)
    return im.shape[:2]

# print(size("lena/lena_std.png"))
# print(size("lena/lena_gray.png"))
# print(size("lena/lena_25_eye.png"))

"""
3 - Crie uma função chamada rgb2gray, que recebe uma imagem RGB e retorna outra
imagem igual à imagem de entrada convertida para escala de cinza. Para converter um pixel
de RGB para escala de cinza, faça a média ponderada dos valores (R, G, B) com os pesos
(0.299, 0.587, 0.114) respectivamente.
ATENÇÃO: verifique se a imagem de entrada permanece inalterada após o término da
execução.
"""

def rgb2gray(filename):
    im = imread(filename)
    gray = np.dot(im[...,:3], [0.299,0.587,0.114])
    gray = gray.astype(np.uint8)
    return gray

# imshow(rgb2gray("lena/lena_std.png"))
# aux_show("lena/lena_std.png")

"""
4 - Crie uma função chamada imreadgray, que recebe um nome de arquivo e retorna a 
imagem lida em escala de cinza. Deve funcionar com imagens de entrada RGB e escala de 
cinza.
"""
def imreadgray(filename):
    im = imread(filename)
    return im if nchannels(filename) == 2 else rgb2gray(filename)
     

# print(imreadgray("lena/lena_gray.png"))
# print(imreadgray("lena/lena_std.png"))