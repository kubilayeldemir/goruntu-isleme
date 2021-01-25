import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import data, io, filters, color, exposure, transform, morphology, util, segmentation
from imageSelector import *

def active_contour():
    img = data.astronaut()
    img=read_image_return_scikit()
    img = color.rgb2gray(img)

    s = np.linspace(0, 2*np.pi, 400)
    r = 250 + 300*np.sin(s)
    c = 310 + 300*np.cos(s)
    init = np.array([r, c]).T

    snake = segmentation.active_contour(filters.gaussian(img, 5),
                        init, alpha=0.015, beta=10, gamma=0.001,max_iterations=5000)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.imshow(img, cmap=plt.cm.gray)
    ax.plot(init[:, 1], init[:, 0], '--r', lw=3)
    ax.plot(snake[:, 1], snake[:, 0], '-b', lw=3)
    ax.set_xticks([]), ax.set_yticks([])
    ax.axis([0, img.shape[1], img.shape[0], 0])

    plt.show()

def cv_active_cont():
    img = read_image_return()
    

    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgray = cv2.GaussianBlur(imgray, (5, 5), 0)
    imgray = cv2.Canny(imgray, 30, 200)

    #cv2.imshow('Image', imgray)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_FLOODFILL, cv2.CHAIN_APPROX_SIMPLE)
    print("Number of contours = " + str(len(contours)))
    print(contours[0])

    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    #cv2.drawContours(imgray, contours, -1, (153, 38, 0), 3)
    setGlobalVar(imgray)
    cv2.imshow('Image', img)
    #cv2.imshow('Image GRAY', imgray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
