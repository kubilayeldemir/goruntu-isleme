import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from skimage import data, io, filters, color, exposure, transform
from imageSelector import *


def rescale_intensity():
    image = read_image_return_scikit()
    print("intensity in range 1.parameter")
    input_a = int(input())
    print("intensity in range 2.parameter")
    input_b = int(input())
    print("intensity out range 1.parameter")
    input_c = int(input())
    print("intensity out range 2.parameter")
    input_d = int(input())
    rescaled = exposure.rescale_intensity(
        image, in_range=(input_a, input_b), out_range=(input_c, input_d))
    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),
                                   sharex=True, sharey=True)

    ax0.imshow(image, cmap=plt.cm.gray)
    ax0.axis('off')
    ax1.imshow(rescaled, cmap=plt.cm.gray)
    ax1.axis('off')

    plt.show()
