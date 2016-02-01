
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

    # Create two lsits. First list will be used to facial recognition for the 6 actors/actress' while the gender
    # mapping has a hardcoded gender for each of the recepients and that will be used for gender classification
    person_mapping = {"butler":0, "radcliffe":1, "vartan":2, "bracco":3, "gilpin":4, "harmon":5}
    gender_mapping = {"richter":1,"elwes":2,"dlein":3,"noth":4,"radcliffe":5,"dourdan":6,"butler":7,
                      "statham":8,"smith":9,"diCaprio":10,"long":11,"gray":12,"vartan":13,"walker":14,
                      "madden":15,"anderson":16,"bracco":17,"cattrall":18,"marie":19,"conn":20,"delany":21,
                      "electra":22,"gilpin":23,"harmon":24,"hartley":25,"hatcher":26,"innes":27,"louis-Dreyfus":28,
                      "marcil":29,"meyer":30}
    
    dir_of_cropped = os.getcwd()+"/cropped2"
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
    for i in range(1,20):
    
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
