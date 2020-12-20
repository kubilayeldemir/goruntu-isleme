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
#print(read_image_meta(r"C:\Users\Kubilay\Desktop\gc\asd.png"))

#show_image(read_image_meta(r"C:\Users\Kubilay\Desktop\gc\asd.png"))
#white_tophat()
#black_tophat()
#skeletonize()
#convex_hull()
#generateElements()
#video()
#cv_active_cont()
global org_image
root = Tk()

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image", command=select_image)

btnWrite = Button(root, text="Write Image", command=save_image)
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
videoBtn = Button(root, text="Video Edge Find- press q to exit", command=lambda:  video())
#-----------------------------------------------------------------------------------------------------------------
videoBtn.pack(side="bottom",expand="no", padx="0", pady="10")
cv_active_contBtn.pack(side="bottom", expand="no", padx="0", pady="10")
objectBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
skeletonizeBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
convex_hullBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
white_tophatBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
black_tophatBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
area_closingBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
intensityBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
generateElementsBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
swirlBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
cropBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
rotateBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
resizeBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
histogramEqBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
histogramBtn.pack(side="bottom",  expand="no", padx="0", pady="10")
multiOtsu.pack(side="bottom",  expand="no", padx="0", pady="10")
edgeOperators.pack(side="bottom",  expand="no", padx="0", pady="10")
hysteresisThreshold.pack(side="bottom",  expand="no", padx="0", pady="10")
btnNiblack.pack(side="bottom",  expand="no", padx="0", pady="10")
btnRidgeOperators.pack(side="bottom",  expand="no", padx="0", pady="10")
btnRidgeOperatorsSelectImg.pack(side="bottom",  expand="no", padx="0", pady="10")
btn.pack(side="bottom",  expand="no", padx="0", pady="10")
btnRead.pack(side="bottom",  expand="no", padx="0", pady="10")
btnWrite.pack(side="bottom",expand="no",padx="0",pady="10")
# kick off the GUI
root.mainloop()
