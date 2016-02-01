
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
from helpers import *

if __name__ == "__main__":
    # Create the empty sets for training, testing and validifying
    trainingSet = {}
    testSet = {}
    validationSet = {}

    person_mapping = {"butler":0, "radcliffe":1, "vartan":2, "bracco":3, "gilpin":4, "harmon":5}
    dir_of_cropped = os.getcwd()+"/cropped"
    get_data(dir_of_cropped, trainingSet, testSet, validationSet, person_mapping)
    
    successful_count = 0
    total_count = 0
    #print len(testSet[1])
    #print len(trainingSet[1])
    #print len(validationSet[1])
    trainingSet, testSet, validationSet = transform_info(trainingSet, testSet, validationSet)
      
    #print len(testSet)
    #print len(validationSet)
    #print len(trainingSet)
    total_correct = 0
    total_tried = 0
    for i in range(1,40):
    
        for test_case in testSet:
            #imshow(test_case)
            nearest_neighbours, lengths = k_neighbours(test_case, trainingSet, i)
            #print lengths
            #print nearest_neighbours
            nearest_neighbours.sort()
            #nearest_neighbours.reverse()
            predicted_type = predict(nearest_neighbours)
            #print "PREDICTED:  "+str(predicted_type) + "ACTUAL " + str(test_case[1])
	
	    if(predicted_type == test_case[1]):
                successful_count +=1
            total_count+=1
        print "for "+str(i) +" as k, we got " + str(successful_count) + " out of " + str(total_count)

        successful_count = 0
        total_count = 0
