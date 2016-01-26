
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import random
import time
from scipy.misc import imsave
from scipy.misc import imread
from scipy.misc import imresize
import matplotlib.image as mpimg
import os
from scipy.ndimage import filters
import urllib


'''
This python file contains all the functions that will be used to handle data files, check for k neighbours
it's repsonse, the accuracy, as weel as statistical graphs
'''

def get_data(filename, trainingSet, testSet, validationSet, person_mapping):
    '''
    This function looks inside the cropped images directory and constructs two lists. First list contains the images 
    while the second list contains what actor/actress it is. The following are the values for each actor/actress:
    Gerard Butler        = 1
    Daniel Radcliffe     = 2
    Michael Vartan       = 3
    Lorraine Bracco      = 4 
    Peri Gilpin          = 5
    Angie Harmon         = 6
    '''

    # Make a empty set for each of the 6 categories which will be filled in later
    fullSet = {}
    for num in range(1,7):
        trainingSet[num] = []
        testSet[num] = []
        validationSet[num] = []
    	fullSet[num] = []
    training_needed = 100
    test_needed = 10
    validation_needed = 10
    
    # Take each cropped image and grey scale it and then change its size to 32 by 32
    for image_name in os.listdir(filename):
        image = imread(filename+"/"+image_name)
	grey_image = rgb2gray(image)
	grey_32 = imresize(grey_image, (32,32))
	value = actor_actress_value(image_name, person_mapping)
        fullSet[value].append(grey_32)
    # To check if elements were put in right category 
    '''
    for num in range(1,7):
        print len(fullSet[num]) 
    '''

    for num in range(1,7):
        trainingSet[num] = fullSet[num][0:100]
        testSet[num] = fullSet[num][100:110]
        validationSet[num] = fullSet[num][110:120]
	
def actor_actress_value(file_name, person_mapping):
    '''
    Given the file name and the mapping, return what actor/actress category the image falls under
    '''  
    elements = file_name.split("_")
    return person_mapping[elements[1]]
 
def rgb2gray(rgb):
    '''Return the grayscale version of the RGB image rgb as a 2D numpy array
    whose range is 0..1
    Arguments:
    rgb -- an RGB image, represented as a numpy array of size n x m x 3. The
    range of the values is 0..255
    '''
    if(len(rgb.shape) == 2):
        return rgb    
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray/255.

