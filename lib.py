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
    print(im)
    return im


# a) Abra uma imagem colorida e a exiba usando o Python Shell.
def openIMG(filename):
    im = Image.open(filename)
    im.show()


# b) Abra uma imagem em escala de cinza e a exiba usando o Python Shell.
def openIMG_gray(filename):
    im = Image.open(filename).convert("L")
    im.show()


# c) Abra uma imagem pequena, com até 50 pixels de lado, e a exiba usando o Python Shell.
def open_small_image(filename):
    im = Image.open(filename)
    width, height = im.size
    if width > 50 or height > 50:
        max_size = (50, 50)
        im.thumbnail(max_size)
    im.show()


"""
0.3 - Crie uma função chamada imshow que recebe uma imagem como parâmetro e a exibe.
Se a imagem for em escala de cinza, exiba com colormap gray. Sempre usar interpolação
nearest para que os pixels apareçam como quadrados ao dar zoom ou exibir imagens
pequenas
"""


def imshow(filename):
    def imshow_aux(im):
        if im.mode == "L":
            mp.imshow(im, cmpa="gray", interpolation="nearest")
        else:
            mp.imshow(im, interpolation="nearest")
        mp.axis("off")
        mp.show()

    imshow_aux(Image.open(filename))


"""
1 - Crie uma função chamada nchannels que retorna o número de canais da imagem de
entrada.
"""


# Dúvida
def nchannels(filename):
    im = Image.open(filename)
    channels = len(im.getbands())
    print(channels)
    return channels


"""
2 - Crie uma função chamada size que retorna um vetor onde a primeira posição é a largura
e a segunda é a altura em pixels da imagem de entrada.
"""


def size(filename):
    im = Image.open(filename)
    wid, hei = im.size
    out = [wid, hei]
    print(out)
    return out


"""
3 - Crie uma função chamada rgb2gray, que recebe uma imagem RGB e retorna outra
imagem igual à imagem de entrada convertida para escala de cinza. Para converter um pixel
de RGB para escala de cinza, faça a média ponderada dos valores (R, G, B) com os pesos
(0.299, 0.587, 0.114) respectivamente.
ATENÇÃO: verifique se a imagem de entrada permanece inalterada após o término da
execução.
"""


# Dúvida
def rgb2gray(filename):
    im = Image.open(filename)
    im_gray = Image.new("L", im.size)

    pixels_im = im.load()
    pixels_im_g = im_gray.load()

    for x in range(im.width):
        for y in range(im.height):
            print(pixels_im[x, y])
            r, g, b = pixels_im[x, y]
            in_gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            pixels_im_g[x, y] = in_gray
    im_gray.show()
    return im_gray


rgb2gray("rgb.png")
# img de teste
i32 = np.array([[1.0, 0.2, 0.56], [0.87, 0.75, 0.98]])
i8 = np.array([[255, 0, 1], [254, 2, 255], [255, 12, 250]])

"""
3 - Seja img uma imagem do tipo ndarray, com pixels de tipo float32 no intervalo [0.0, 1.0]. Escreva uma
linha de código em Python que converta seus pixels para o tipo uint8 no intervalo [0, 255].
"""


def normalize(I):
    out = (I * 255).astype(np.uint8)
    print(out)
    return out


"""
4 - Seja img uma imagem do tipo ndarray, com pixels de tipo uint8. Escreva uma linha de código em Python
que encontre sua negativa.
"""


def negative(I):
    out = 256 - I - 1
    print(out)
    return out


"""
5 - Considere o código em Python abaixo. Insira código no lugar das reticências para fazer a saturação em 0 e
255, e converter para uint8.
"""


def contrast(im, r, m):
    result = r * (im - m) + m
    # im = 0 if im <= 0
    # im = 255 if im >= 255
    # print(result)
    return result


# normalize(i32)
# print("\n\n\n")
# negative(i8)
