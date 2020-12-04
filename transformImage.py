import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from skimage import data, io, filters, color, exposure, img_as_float, img_as_ubyte
from imageSelector import *

def resize():
    image = data.camera()
    resize(image, (100, 100)).shape
