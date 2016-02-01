'''
This python file contains all the functions that will be used to handle data files, check for k neighbours
it's repsonse, the accuracy, as weel as statistical graphs
'''

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import random
import time
from scipy.misc import imshow
from scipy.misc import imsave
from scipy.misc import imread
from scipy.misc import imresize
import matplotlib.image as mpimg
import os
from scipy.ndimage import filters
import urllib
import math

def predict_actor_ress(list_of_neighbours):
    '''
    list_of_neighbours contains a list of nearest elements to k. Since we are attempting to predict the type
    of actor, we can simply search for the maxium actor occurance in the list and take that to be the actor. 
    There won't be any ties since we set our k values to be odd, so any potential ties will be broken.
    '''
    predicted = [0,0,0,0,0,0]
    for neighbour in list_of_neighbours:

        predicted[neighbour-1] = predicted[neighbour-1] + 1
    return predicted.index(max(predicted)) + 1

def predict_gender(list_of_neighbours):
    predicted = [0,0]
    #print list_of_neighbours
    for neighbour in list_of_neighbours:
        
        predicted[neighbour] = predicted[neighbour]+1
    return predicted.index(max(predicted))

def k_neighbours(point, list_of_elements, k):
    '''
    Returns the k closest elements to element a
    '''
    neighbours_lengths = []
    elements_in_list = []
    for element in list_of_elements:
        # At this point, element will be of form (double_list, integer)
        #distance = eculideanDistance(point, element)
        distance = distance_get(point,element)
        if(len(neighbours_lengths) < k):
            neighbours_lengths.append(distance)
            elements_in_list.append(element[1])
        else:
            maximum_distance = max(neighbours_lengths)
            #print "max dist: "+str(maximum_distance)+" | current is "+str(distance)
            if(maximum_distance >= distance):
                maximum_element_index = neighbours_lengths.index(maximum_distance)
                neighbours_lengths[maximum_element_index] = distance
                elements_in_list[maximum_element_index] = element[1]
    #print elements_in_list
    #print predict(elements_in_list)    
    return elements_in_list, neighbours_lengths 
    
         
def transform_info(trainingSet, testSet, validationSet):
    '''
    Transforming all information to form (image, actor_value) so it's easier to find k_neighbours    
    '''
    temp_training = trainingSet
    temp_set = testSet
    temp_validation = validationSet
    
    trainingSet = []
    testSet = []
    validationSet = []

    for element in temp_training:
        for group in temp_training[element]:
            trainingSet.append((group,element))

    for element in temp_set:
        for group in temp_set[element]:
            testSet.append((group,element))

    for element in temp_validation:
        for group in temp_validation[element]:
            validationSet.append((group,element))
    
    #print str(len(trainingSet)) + " " + str(len(testSet)) + " " + str(len(validationSet))

    return trainingSet,testSet,validationSet

def distance_get(a,b):
    math_sum = (np.array(a[0])-np.array(b[0]))**2
    return math.sqrt(math_sum.sum())  


def eculideanDistance(set1, set2):
    '''
    Computes the Euclidean distance matrix between a and b.
    '''
    a = set1[0].flatten()
    b = set2[0].flatten()
    if a.shape[0] != b.shape[0]:
        raise ValueError("A and B should be of same dimensionality")

    aa = np.sum(a**2, axis=0)
    bb = np.sum(b**2, axis=0)
    ab = np.dot(a.T, b)
    return np.sqrt(aa[:, np.newaxis] + bb[np.newaxis, :] - 2*ab)


def get_data_gender(filename, trainingSet, testSet, validationSet, person_mapping):
    '''
    This function looks inside the cropped images directory and constructs two lists. First list contains the images 
    while the second list contains what actor/actress it is. The following are the values for each actor/actress:

    '''

    # Make a empty set for each of the 6 categories which will be filled in later
    fullSet = {}
    for num in range(0,2):
        trainingSet[num] = []
        testSet[num] = []
    	validationSet[num] = []
#{"butler":0, "radcliffe":1, "vartan":2, "bracco":3, "gilpin":4, "harmon":5}    
    # Take each cropped image and grey scale it and then change its size to 32 by 32
    for image_name in os.listdir(filename):
        image = imread(filename+"/"+image_name)
	value = actor_actress_value(image_name, person_mapping)
        name = image_name.split("_")
        if(name[1] in ["butler","radcliffe","vartan","bracco","gilpin","harmon"]):
            #print validationSet
            if(len(validationSet[value]) < 10):
                validationSet[value].append(image)
            else:
                trainingSet[value].append(image)
        else:
            testSet[value].append(image)
    return trainingSet, validationSet, testSet       
 


def get_data_mini_gender(filename, trainingSet, testSet, validationSet, person_mapping):
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
    for num in range(0,2):
        trainingSet[num] = []
        testSet[num] = []
        validationSet[num] = []
    	fullSet[num] = []
    training_needed = 90
    test_needed = 10
    validation_needed = 10
    
    # Take each cropped image and grey scale it and then change its size to 32 by 32
    for image_name in os.listdir(filename):
        image = imread(filename+"/"+image_name)
	value = actor_actress_value(image_name, person_mapping)
        if(value != 999):
            fullSet[value].append(image)
    
    # Populate the training, test, and validation sets but don't overlap any elements
    for num in range(0,2):
        trainingSet[num] = fullSet[num][0:training_needed]
        testSet[num] = fullSet[num][training_needed:training_needed+test_needed]
        validationSet[num] = fullSet[num][training_needed+test_needed:training_needed+test_needed+validation_needed]
    return trainingSet, validationSet, testSet 


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
    for num in range(0,6):
        trainingSet[num] = []
        testSet[num] = []
        validationSet[num] = []
    	fullSet[num] = []
    training_needed = 90
    test_needed = 10
    validation_needed = 10
    
    # Take each cropped image and grey scale it and then change its size to 32 by 32
    for image_name in os.listdir(filename):
        image = imread(filename+"/"+image_name)
	value = actor_actress_value(image_name, person_mapping)
        if(value != 999):
            fullSet[value].append(image)
    
    # Populate the training, test, and validation sets but don't overlap any elements
    for num in range(0,6):
        trainingSet[num] = fullSet[num][0:training_needed]
        testSet[num] = fullSet[num][training_needed:training_needed+test_needed]
        validationSet[num] = fullSet[num][training_needed+test_needed:training_needed+test_needed+validation_needed]
        #print num
        #print len(testSet[num])
        #print len(trainingSet[num])
        #print len(validationSet[num])
	
def actor_actress_value(file_name, person_mapping):
    '''
    Given the file name and the mapping, return what actor/actress category the image falls under
    '''  
    elements = file_name.split("_")
    #print file_name + "    " + str(person_mapping[elements[1]])
    if(elements[1] in person_mapping.keys()):
        return person_mapping[elements[1]]
    #print file_name    
    return 999
 
def rgb2gray(rgb):
    '''
    Return the grayscale version of the RGB image rgb as a 2D numpy array
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

