
from application.calculations.features.feature_color import getColorFeature
from application.calculations.features.feature_gabor import *
from application.calculations.features.feature_moments import getShapeFeatures
from application.calculations.features.img_seg import *

def createFeature(img):
	'''
	Creates the feature vector of the image using the three features -
	color, texture, and shape features
	'''
	feature = []
	areaFruit, binaryImg, colourImg, areaSkin, fruitContour, pix_to_cm_multiplier = getAreaOfFood(img)
	color = getColorFeature(colourImg)
	texture = getTextureFeature(colourImg)
	shape = getShapeFeatures(binaryImg)
	for i in color:
		feature.append(i)
	for i in texture:
		feature.append(i)
	for i in shape:
		feature.append(i)
	
	M = max(feature)
	m = min(feature)
	feature = list(map(lambda x: x * 2, feature))
	feature = (feature - M - m)/(M - m)
	mean=np.mean(feature)
	dev=np.std(feature)
	feature = (feature - mean)/dev

	return feature, areaFruit, areaSkin, fruitContour, pix_to_cm_multiplier

def readFeatureImg(filename):
	'''
	Reads an input image when the filename is given,
	and creates the feature vector of the image.
	'''
	img = cv2.imread(filename)
	f, farea, skinarea, fcont, pix_to_cm = createFeature(img)
	return f, farea, skinarea, fcont, pix_to_cm

if __name__ == '__main__':
	import sys
	f = readFeatureImg(sys.argv[1])
	print(f, len(f))
