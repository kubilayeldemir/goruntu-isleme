import cv2 as cv
from matplotlib import pyplot as plt
from skimage import data, io, filters,color
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
