import numpy as np
import cv2 as cv
from skimage import data, io, filters, color
from tkinter import filedialog
from tkinter import *
from imageSelector import *
from PIL import Image
from PIL import ImageTk
from imageFilters import *
#print(read_image_meta(r"C:\Users\Kubilay\Desktop\gc\asd.png"))

#show_image(read_image_meta(r"C:\Users\Kubilay\Desktop\gc\asd.png"))


global org_image
root = Tk()

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image", command=select_image)

btnWrite = Button(root, text="Write Image", command=save_image)
btnRead = Button(root, text="Read Image", command=read_image)
btnRidgeOperators = Button(root, text="Ridge Operator(Filters)", command=ridge_operators)

btnRidgeOperatorsSelectImg = Button(root, text='Ridge Operator(Filters-Select Image)', command= lambda: ridge_operators_select(read_image_return()))

btnRidgeOperators.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
btnRidgeOperatorsSelectImg.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
btn.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
btnRead.pack(side="bottom", fill="both", expand="no", padx="0", pady="10")
btnWrite.pack(side="bottom",fill="both",expand="no",padx="0",pady="10")
# kick off the GUI
root.mainloop()

""" path=select_image()

img = cv.imread(path)
cv.imshow('sa',img)

cv.destroyAllWindows()
a=0


b="sa"

b=b.capitalize()
print(b)
 """
""" ctrl """
