import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from skimage import data, io, filters, color, exposure, img_as_float, img_as_ubyte
from imageSelector import *


def niblack_threshold(image):
	gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	#show_image(gray)
	threshold_image = filters.threshold_niblack(gray, window_size=7, k=0.1)	
	show_image(threshold_image)


def hysteresis_threshold(image):
	fig, ax = plt.subplots(nrows=2, ncols=2)	
	image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	edges = filters.sobel(image)

	low = 0.1
	high = 0.35

	lowt = (edges > low).astype(int)
	hight = (edges > high).astype(int)
	hyst = filters.apply_hysteresis_threshold(edges, low, high)

	ax[0, 0].imshow(image, cmap='gray')
	ax[0, 0].set_title('Original image')

	ax[0, 1].imshow(edges, cmap='magma')
	ax[0, 1].set_title('Sobel edges')

	ax[1, 0].imshow(lowt, cmap='magma')
	ax[1, 0].set_title('Low threshold')

	ax[1, 1].imshow(hight + hyst, cmap='magma')
	ax[1, 1].set_title('Hysteresis threshold')

	for a in ax.ravel():
		a.axis('off')

	plt.tight_layout()

	plt.show()
	
def sato(image):
	image= data.coins()
	image = filters.sato(image, sigmas=range(1, 10, 2), black_ridges=True, mode=None, cval=0)
	cmap = plt.cm.gray
	fig, axes = plt.subplots(1, 1, squeeze=False)
	axes[0, 0].imshow(image, cmap=cmap, aspect='auto')
	plt.tight_layout()
	plt.show()
	
def ridge_operators_select(image):	
	image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	cmap = plt.cm.gray
	kwargs = {'sigmas': [1], 'mode': 'reflect'}
	try:
		fig, axes = plt.subplots(2, 5)
		for i, black_ridges in enumerate([1, 0]):
			for j, func in enumerate([filters.meijering, filters.sato, filters.frangi, filters.hessian]):
				kwargs['black_ridges'] = black_ridges
				result = func(image, **kwargs)
				axes[i, j].imshow(result, cmap=cmap, aspect='auto')
				if i == 0:
					axes[i, j].set_title(['Original\nimage', 'Meijering\nneuriteness',
										'Sato\ntubeness', 'Frangi\nvesselness',
										'Hessian\nvesselness'][j])
				if j == 0:
					axes[i, j].set_ylabel('black_ridges = ' + str(bool(black_ridges)))
				axes[i, j].set_xticks([])
				axes[i, j].set_yticks([])

		plt.tight_layout()
		plt.show()
	except Exception as e:
		print(e.args)
		print("Image is not eligible for this process")
		quit()

def ridge_operators():  # Ridge operators meijering, sato, frangi, hessian
	image = color.rgb2gray(data.retina())[300:700, 700:900]	
	cmap = plt.cm.gray
	kwargs = {'sigmas': [1], 'mode': 'reflect'}
	
	fig, axes = plt.subplots(2, 5)
	for i, black_ridges in enumerate([1, 0]):
		for j, func in enumerate([filters.meijering, filters.sato, filters.frangi, filters.hessian]):
			kwargs['black_ridges'] = black_ridges
			result = func(image, **kwargs)
			axes[i, j].imshow(result, cmap=cmap, aspect='auto')
			if i == 0:
				axes[i, j].set_title(['Original\nimage', 'Meijering\nneuriteness',
									'Sato\ntubeness', 'Frangi\nvesselness',
									'Hessian\nvesselness'][j])
			if j == 0:
				axes[i, j].set_ylabel('black_ridges = ' + str(bool(black_ridges)))
			axes[i, j].set_xticks([])
			axes[i, j].set_yticks([])

	plt.tight_layout()
	plt.show()


def edge_operators(image):
	image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	edge_roberts = filters.roberts(image)
	edge_sobel = filters.sobel(image)

	fig, axes = plt.subplots(ncols=2, sharex=True, sharey=True,
							figsize=(8, 4))

	axes[0].imshow(edge_roberts, cmap=plt.cm.gray)
	axes[0].set_title('Roberts Edge Detection')

	axes[1].imshow(edge_sobel, cmap=plt.cm.gray)
	axes[1].set_title('Sobel Edge Detection')

	for ax in axes:
		ax.axis('off')

	plt.tight_layout()
	plt.show()


def laplace(image):
	image=filters.laplace(image, ksize=3, mask=None)
	print(image)
	show_image(image)


def multi_otsu(image):
	image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	# Applying multi-Otsu threshold for the default value, generating
	# three classes.
	thresholds = filters.threshold_multiotsu(image)

	# Using the threshold values, we generate the three regions.
	regions = np.digitize(image, bins=thresholds)

	fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 3.5))

	# Plotting the original image.
	ax[0].imshow(image, cmap='gray')
	ax[0].set_title('Original')
	ax[0].axis('off')

	# Plotting the Multi Otsu result.
	ax[1].imshow(regions, cmap='jet')
	ax[1].set_title('Multi-Otsu result')
	ax[1].axis('off')

	plt.subplots_adjust()

	plt.show()


def histogram():
	img=read_image_return()
	hist, bins = np.histogram(img.flatten(), 256, [0, 256])
	cdf = hist.cumsum()
	cdf_normalized = cdf * hist.max() / cdf.max()

	plt.plot(cdf_normalized, color='b')
	plt.hist(img.flatten(), 256, [0, 256], color='r')
	plt.xlim([0, 256])
	plt.legend(('cdf', 'histogram'), loc='upper left')
	plt.show()

def histogramEquation():
	#reference = data.coffee()
	image=read_image_return()
	reference=read_image_return()

	#image = data.chelsea()

	matched = exposure.match_histograms(image, reference, multichannel=True)

	fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
										sharex=True, sharey=True)
	for aa in (ax1, ax2, ax3):
		aa.set_axis_off()

	ax1.imshow(image)
	ax1.set_title('Source')
	ax2.imshow(reference)
	ax2.set_title('Reference')
	ax3.imshow(matched)
	ax3.set_title('Matched')

	plt.tight_layout()
	plt.show()
