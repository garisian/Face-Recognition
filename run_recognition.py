
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

    person_mapping = {"butler":1, "radcliffe":2, "vartan":3, "bracco":4, "gilpin":5, "harmon":6}
    dir_of_cropped = os.getcwd()+"/cropped"
    get_data(dir_of_cropped, trainingSet, testSet, validationSet, person_mapping)
    
    count = 1
    #print len(testSet[1])
    #print len(trainingSet[1])
    #print len(validationSet[1])
    transformed_info = transform_info(trainingSet, testSet, validationSet)
    #for category in testSet:
    #    for image in testSet[category]:
            
