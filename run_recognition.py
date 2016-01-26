
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
    #for i in os.listdir(os.getcwd()+"/uncropped"):
    #    image = imread(os.getcwd()+"/uncropped/"+i);
    trainingSet = {}
    testSet = {}
    validationSet = {}
    person_mapping = {"butler":1, "radcliffe":2, "vartan":3, "bracco":4, "gilpin":5, "harmon":6}
    dir_of_cropped = os.getcwd()+"/cropped"
    get_data(dir_of_cropped, trainingSet, testSet, validationSet, person_mapping)



