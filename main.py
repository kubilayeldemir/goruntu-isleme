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
#print(read_image_meta(r"C:\Users\Kubilay\Desktop\gc\asd.png"))

#show_image(read_image_meta(r"C:\Users\Kubilay\Desktop\gc\asd.png"))

rescale_intensity()
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
#-----------------------------------------------------------------------------------------------------------------
histogramBtn.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
multiOtsu.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
edgeOperators.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
hysteresisThreshold.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
btnNiblack.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
btnRidgeOperators.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
btnRidgeOperatorsSelectImg.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
btn.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
btnRead.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
btnWrite.pack(side="bottom",fill="both",expand="no",padx="0",pady="10")
# kick off the GUI
root.mainloop()
