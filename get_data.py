
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

#act = list(set([a.split("\t")[0] for a in open("subset_actors.txt").readlines()]))
act = ['Gerard Butler','Daniel Radcliffe','Michael Vartan','Lorraine Bracco','Peri Gilpin','Angie Harmon']

def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    '''From:
    http://code.activestate.com/recipes/473878-timeout-function-using-threading/'''
    import threading
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except:
                self.result = default

    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return False
    else:
        return it.result

testfile = urllib.URLopener()            


#Note: you need to create the uncropped folder first in order 
#for this to work
for a in act:
    # Extract the last name of every person in "a" list
    name = a.split()[1].lower() 
    i = 0
    error = ""
    for line in open("faces_subset.txt"):
    #for line in open("small_file.txt"):
        if a in line:
	    print line
	    filename = name+str(i)+'.'+line.split()[4].split('.')[-1]
	    #A version without timeout (uncomment in case you need to 
            #unsupress exceptions, which timeout() does)
            #testfile.retrieve(line.split()[4], "uncropped/"+filename)
            #timeout is used to stop downloading images which take too long to download
            timeout(testfile.retrieve, (line.split()[4], "uncropped/"+filename), {}, 30)
 
 	    if not os.path.isfile("uncropped/"+filename):
                continue           
	    print filename
	    line_parsed = line.split()[5].split(',');
	    try:
		ids = imread("uncropped/"+filename)
	    except:
		continue
	    print ids.shape
#            print line_parsed
#	    if(ids.shape == (1,1)):
#		error += line + "\n"
#		continue
	    cropped_image = ids[int(line_parsed[0]):int(line_parsed[2]),int(line_parsed[1]):int(line_parsed[3]),];            
	    imsave('cropped/modified_'+filename,cropped_image);
            print 'cropped/modifiend_'+filename+' is SUCCESSFUL';
#	    try:
#                #read each picture and crop it based on the values stated in "line
#              ids = imread("uncropped/"+filename)
#                #print ids.shape
#                #print line            
#                print filename + " successfully put into uncropped"
#                #print ids
#                line_parsed = line.split()[5].split(',')
#                #print line_parsed
#                #print ids.shape
#                cropped_image = ids[int(line_parsed[0]):int(line_parsed[2]),int(line_parsed[1]):int(line_parsed[3]),];
#                imsave('cropped/modified_'+filename,cropped_image);
#                #print line_parsed
#                print 'cropped/modified_'+filename +" successfully put into cropped"  
#	    except:
#  		print 'cropped/modified_'+filename + " FAILED TO BE CROPPED"
            i += 1
#print error
