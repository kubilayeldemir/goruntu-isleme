import numpy as np
import cv2 as cv
from skimage import data, io, filters, color
from tkinter import filedialog
from tkinter import *
from imageSelector import *
from PIL import Image
from PIL import ImageTk
from imageFilters import *
from transformImage import *
from intensity import *
from morphology import *
from video import *
from segmentation import *

global org_image
root = Tk()
root.title("Osman Kubilay Eldemir IP Proje1")


btnWrite = Button(root, text="Save Image", command=save_image)
btnRead = Button(root, text="Read Image", command=read_image)
btnRidgeOperators = Button(root, text="Ridge Operator(Filters)", command=ridge_operators)
btnNiblack = Button(root, text="Niblack Threshold(1)", command= lambda: niblack_threshold(read_image_return()))
btnRidgeOperatorsSelectImg = Button(root, text='Ridge Operator(3)(Filters-Select Image)', command= lambda: ridge_operators_select(read_image_return()))
hysteresisThreshold = Button(root, text="Hysteresis Threshold(3)", command= lambda: hysteresis_threshold(read_image_return()))
edgeOperators = Button(root, text="Edge Operators(2)", command=lambda: edge_operators(read_image_return()))
multiOtsu=Button(root, text="Multi Otsu Threshold", command=lambda: multi_otsu(read_image_return()))
histogramBtn=Button(root, text="Histogram", command=lambda: histogram())
histogramEqBtn = Button(root, text="Histogram Equation", command=lambda:  histogramEquation())
resizeBtn = Button(root, text="Resize 60%", command=lambda:  resize())
rotateBtn = Button(root, text="Rotate 90", command=lambda:  rotate())
cropBtn = Button(root, text="Crop 500x500", command=lambda:  crop())
swirlBtn = Button(root, text="Swirl", command=lambda:  swirl())
generateElementsBtn = Button(root, text="Generate Elements", command=lambda:  generateElements())
intensityBtn = Button(root, text="Intensity", command=lambda:  rescale_intensity())
area_closingBtn = Button(root, text="Area Closing", command=lambda:  area_closing())
black_tophatBtn = Button(root, text="Black Top Hat", command=lambda:  black_tophat())
white_tophatBtn = Button(root, text="White Top Hat", command=lambda:  white_tophat())
convex_hullBtn = Button(root, text="Convex Hull", command=lambda:  convex_hull())
skeletonizeBtn = Button(root, text="skeletonize", command=lambda:  skeletonize())
objectBtn = Button(root, text="Object Morphology", command=lambda:  objects())
cv_active_contBtn = Button(root, text="Active Contour", command=lambda:  cv_active_cont())
effectBtn = Button(root, text="Special Effect", command=lambda:  insta())
videoBtn = Button(root, text="Video Edge Find- press q to exit", command=lambda:  video())
filterslabel=Label(root,text="3)Filtreler")
histogramlabel = Label(root, text="4)Histogram")
transformlabel = Label(root, text="5)Transform")
intensitylabel = Label(root, text="6)Intensity")
morphhologylabel = Label(root, text="7)Morphology")
contourlabel = Label(root, text="8)Active Contour")
videolabel = Label(root, text="10)Video Processing")
readlabel = Label(root, text="1)Read Load")
effectlabel = Label(root, text="9)Instagram Filter")
#-----------------------------------------------------------------------------------------------------------------
effectBtn.grid(row=8, column=1)
effectlabel.grid(row=8, column=0)
videoBtn.grid(row=9, column=1)
videolabel.grid(row=9, column=0)
cv_active_contBtn.grid(row=7, column=1)
contourlabel.grid(row=7, column=0)
objectBtn.grid(row=6, column=5)
skeletonizeBtn.grid(row=6,column=4)
convex_hullBtn.grid(row=6,column=3)
white_tophatBtn.grid(row=6,column=2)
black_tophatBtn.grid(row=6,column=1)
area_closingBtn.grid(row=6,column=6)
morphhologylabel.grid(row=6, column=0)
intensityBtn.grid(row=5,column=1)
intensitylabel.grid(row=5, column=0)
generateElementsBtn.grid(row=4,column=4)
swirlBtn.grid(row=4,column=5)
cropBtn.grid(row=4,column=3)
rotateBtn.grid(row=4,column=2)
resizeBtn.grid(row=4,column=1)
transformlabel.grid(row=4, column=0)
histogramEqBtn.grid(row=3,column=2)
histogramBtn.grid(row=3,column=1)
histogramlabel.grid(row=3, column=0)
multiOtsu.grid(row=1,column=4)
edgeOperators.grid(row=1,column=3)
hysteresisThreshold.grid(row=1, column=2)
btnNiblack.grid(row=1, column=1)
btnRidgeOperators.grid(row=1, column=5)
filterslabel.grid(row=1,column=0)
btnRidgeOperatorsSelectImg.grid(row=1, column=6)
btnRead.grid(row=0, column=1)
btnWrite.grid(row=0,column=2)
readlabel.grid(row=0, column=0)

# kick off the GUI
root.mainloop()
