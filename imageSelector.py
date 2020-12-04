import numpy as np
import cv2 as cv
from tkinter import filedialog
from tkinter import *
from PIL import Image
from PIL import ImageTk
panelA=None
panelB=None
global org_image
def show_image(image):
	cv.imshow('image', image/255)
	cv.waitKey(0)
	cv.destroyAllWindows()

def read_image():
	global org_image
	global panelA
	path = filedialog.askopenfilename()
	if len(path) > 0:
		image = cv.imread(path)
		org_image=cv.imread(path)
		image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
		image = Image.fromarray(image)
		image = ImageTk.PhotoImage(image)
		if panelA is None:
			# the first panel will store our original image
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)			
		# otherwise, update the image panels
		else:
			# update the pannels
			panelA.configure(image=image)			
			panelA.image = image

def read_image_return():
	global org_image	
	path = filedialog.askopenfilename()
	if len(path) > 0:
		image = cv.imread(path)
		#print(image)
		return image
		
def read_image_path(path):
	global org_image
	global panelA
	if len(path) > 0:
		image = cv.imread(path)
		org_image = cv.imread(path)
		return image


def save_image():
	global org_image
	global panelA
	#cl(org_image)
	path = filedialog.asksaveasfilename()
	cv.imwrite(path, org_image, [cv.IMWRITE_JPEG_QUALITY, 95])


def save_image_meta(image):	
	global panelA
	#cl(org_image)
	path = filedialog.asksaveasfilename()
	cv.imwrite(path, image, [cv.IMWRITE_JPEG_QUALITY, 95])

def select_image():
	# grab a reference to the image panels
	global panelA, panelB
	# open a file chooser dialog and allow the user to select an input
	# image
	path = filedialog.askopenfilename()
	if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv.imread(path)		

		#gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
		#edged = cv.Canny(gray, 50, 100)

		#cv.imshow('sa', edged)
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
		# convert the images to PIL format...
		image = Image.fromarray(image)
		org_image = image = Image.fromarray(image)
		edged = Image.fromarray(edged)
		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)

		#edged = ImageTk.PhotoImage(edged)

		if panelA is None or panelB is None:
			# the first panel will store our original image
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
			# while the second panel will store the edge map
			panelB = Label(image=edged)
			panelB.image = edged
			panelB.pack(side="right", padx=10, pady=10)
		# otherwise, update the image panels
		else:
			# update the pannels
			panelA.configure(image=image)
			panelB.configure(image=edged)
			panelA.image = image
			panelB.image = edged
		return org_image
	# initialize the window toolkit along with the two image panels

