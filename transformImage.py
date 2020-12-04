import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from skimage import data, io, filters, color, exposure, transform
from imageSelector import *


def resize(): #%60 kucultuldu
    img = read_image_return()
    print('Original Dimensions : ', img.shape)

    scale_percent = 60  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)

    print('Resized Dimensions : ', resized.shape)

    cv.imshow("Resized image", resized)
    save_image_meta(resized)
    cv.waitKey(0)
    cv.destroyAllWindows()

def rotate():

    src = read_image_return()

    # Window name in which image is displayed
    window_name = 'Image'

    # Using cv2.rotate() method
    # Using cv2.ROTATE_90_CLOCKWISE rotate
    # by 90 degrees clockwise
    image = cv.rotate(src, cv.ROTATE_90_CLOCKWISE)

    # Displaying the image
    cv.imshow(window_name, image)
    save_image_meta(image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def crop():
    img = read_image_return()
    crop_img = img[0:500, 0:500]
    cv.imshow("cropped", crop_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def shift_left(xy):
    xy[:, 0] += 50
    return xy

def swirl():    
    image = read_image_return()
    swirled = transform.swirl(image, rotation=0, strength=10, radius=500)

    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),
                                sharex=True, sharey=True)

    ax0.imshow(image, cmap=plt.cm.gray)
    ax0.axis('off')
    ax1.imshow(swirled, cmap=plt.cm.gray)
    ax1.axis('off')

    plt.show()
