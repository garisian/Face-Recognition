
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

    dir_of_cropped = os.getcwd()+"/cropped2"
    get_data(dir_of_cropped, trainingSet, testSet, validationSet, person_mapping)
    
    successful_count = 0
    total_count = 0
    trainingSet, testSet, validationSet = transform_info(trainingSet, testSet, validationSet)
    #print len(trainingSet)
    #print len(testSet)
    #print len(validationSet)

    for i in range(1,20):
    
        for test_case in testSet:
            #imshow(test_case)
            nearest_neighbours, lengths = k_neighbours(test_case, trainingSet, i)
            nearest_neighbours.sort()
            predicted_type = predict_actor_ress(nearest_neighbours)
	
	    if(predicted_type == test_case[1]):
                successful_count +=1
            total_count+=1
        print "for "+str(i) +" as k, we got " + str(successful_count) + " out of " + str(total_count)

        successful_count = 0
        total_count = 0


    #---------------------------------------------------------------------------------------


    # Create two lsits. First list will be used to facial recognition for the 6 actors/actress' while the gender
    # mapping has a hardcoded gender for each of the recepients and that will be used for gender classification
    gender_mapping = {"butler":1, "radcliffe":1, "vartan":1, "bracco":0, "gilpin":0, "harmon":0}
    trainingSet = {}
    testSet = {}
    validationSet = {}
    dir_of_cropped = os.getcwd()+"/cropped2"
    trainingSet, validationSet, testSet = get_data_mini_gender(dir_of_cropped, trainingSet, testSet, validationSet, gender_mapping)
    successful_count = 0
    total_count = 0

    trainingSet, testSet, validationSet = transform_info(trainingSet, testSet, validationSet)



    for i in range(1,20):    
        for test_case in testSet:
            #imshow(test_case)
            nearest_neighbours, lengths = k_neighbours(test_case, trainingSet, i)
            nearest_neighbours.sort()
            predicted_type = predict_gender(nearest_neighbours)
	
	    if(predicted_type == test_case[1]):
                successful_count +=1
            total_count+=1
        print "for "+str(i) +" as k, we got " + str(successful_count) + " out of " + str(total_count)

        successful_count = 0
        total_count = 0

	



    #---------------------------------------------------------------------------------------


    # Create the empty sets for training, testing and validifying
    trainingSet = {}
    testSet = {}
    validationSet = {}

    # Create two lsits. First list will be used to facial recognition for the 6 actors/actress' while the gender
    # mapping has a hardcoded gender for each of the recepients and that will be used for gender classification
    gender_mapping = {"anderson": 0,"bracco": 0,"butler":1,"cattrall":0,"conn":0,"delany":0,"dicaprio":1,"dourdan":1,
                      "electra":0,"elwes":1,"gilpin":0,"gray":1,"harmon":0,"hartley":0,"hatcher":0,"innes":0,
                      "klein":1,"long":1,"louis-dreyfus":1,"madden":1,"marcil":0,"marie":0,"meyer":0,"noth":1,
                      "radcliffe":1,"richter":1,"smith":1,"statham":1,"vartan":1,"walker":1}

    dir_of_cropped = os.getcwd()+"/cropped2"
    trainingSet, validationSet, testSet = get_data_gender(dir_of_cropped, trainingSet, testSet, validationSet, gender_mapping)
 
    successful_count = 0
    total_count = 0

    trainingSet, testSet, validationSet = transform_info(trainingSet, testSet, validationSet)
    #print len(trainingSet)
    #print len(testSet)
    #print len(validationSet)
    for i in range(1,20):    
        for test_case in testSet:
            #imshow(test_case)
            nearest_neighbours, lengths = k_neighbours(test_case, trainingSet, i)
            nearest_neighbours.sort()
            predicted_type = predict_gender(nearest_neighbours)
	
	    if(predicted_type == test_case[1]):
                successful_count +=1
            total_count+=1
        print "for "+str(i) +" as k, we got " + str(successful_count) + " out of " + str(total_count)

        successful_count = 0
        total_count = 0

    #---------------------------------------------------------------------------------------


