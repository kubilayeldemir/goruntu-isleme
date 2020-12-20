import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from skimage import data, io, filters, color, exposure, transform,morphology,util
from imageSelector import *

def area_closing():
    image = read_image_return_scikit()
    closed = morphology.area_closing(image,area_threshold=1, connectivity=1)
    
    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),
                                   sharex=True, sharey=True)

    ax0.imshow(image, cmap=plt.cm.gray)
    ax0.axis('off')
    ax1.imshow(closed, cmap=plt.cm.gray)
    ax1.axis('off')

    plt.show()


def black_tophat():
    image = io.imread("pics/Cosmos.jpg")
    blacked = morphology.black_tophat(image)
    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),
                                sharex=True, sharey=True)

    ax0.imshow(image, cmap=plt.cm.gray)
    ax0.axis('off')
    ax1.imshow(blacked, cmap=plt.cm.gray)
    ax1.axis('off')

    plt.show()

def white_tophat():
    image = io.imread("pics/Cosmos.jpg")
    white = morphology.white_tophat(image)
    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),
                                   sharex=True, sharey=True)

    ax0.imshow(image, cmap=plt.cm.gray)
    ax0.axis('off')
    ax1.imshow(white, cmap=plt.cm.gray)
    ax1.axis('off')

    plt.show()


def convex_hull():

    # The original image is inverted as the object must be white.
    image = util.invert(data.horse())

    chull = morphology.convex_hull_image(image)

    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    ax = axes.ravel()

    ax[0].set_title('Original picture')
    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].set_axis_off()

    ax[1].set_title('Transformed picture')
    ax[1].imshow(chull, cmap=plt.cm.gray)
    ax[1].set_axis_off()

    plt.tight_layout()
    plt.show()


def skeletonize():    
    image = util.invert(data.horse())  
    # perform skeletonization
    skeleton = morphology.skeletonize(image)

    # display results
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
                            sharex=True, sharey=True)

    ax = axes.ravel()

    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].axis('off')
    ax[0].set_title('original', fontsize=20)

    ax[1].imshow(skeleton, cmap=plt.cm.gray)
    ax[1].axis('off')
    ax[1].set_title('skeleton', fontsize=20)

    fig.tight_layout()
    plt.show()


def objects():
    from skimage.morphology import (square, rectangle, diamond, disk, cube,
                                    octahedron, ball, octagon, star)
    from mpl_toolkits.mplot3d import Axes3D
    # Generate 2D and 3D structuring elements.
    struc_2d = {
        "square(15)": square(15),
        "rectangle(15, 10)": rectangle(15, 10),
        "diamond(7)": diamond(7),
        "disk(7)": disk(7),
        "octagon(7, 4)": octagon(7, 4),
        "star(5)": star(5)
    }

    struc_3d = {
        "cube(11)": cube(11),
        "octahedron(5)": octahedron(5),
        "ball(5)": ball(5)
    }

    # Visualize the elements.
    fig = plt.figure(figsize=(8, 8))

    idx = 1
    for title, struc in struc_2d.items():
        ax = fig.add_subplot(3, 3, idx)
        ax.imshow(struc, cmap="Paired", vmin=0, vmax=12)
        for i in range(struc.shape[0]):
            for j in range(struc.shape[1]):
                ax.text(j, i, struc[i, j], ha="center", va="center", color="w")
        ax.set_axis_off()
        ax.set_title(title)
        idx += 1

    for title, struc in struc_3d.items():
        ax = fig.add_subplot(3, 3, idx, projection=Axes3D.name)
        ax.voxels(struc)
        ax.set_title(title)
        idx += 1

    fig.tight_layout()
    plt.show()
