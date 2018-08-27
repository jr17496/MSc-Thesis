#from Import import  Import
#from ICA import ICA
import numpy as np
import mne
import pyedflib

from matplotlib import pyplot as plt

filename = 'data.bdf'

from Load_from_file.Preproc import Preprocess
from Load_from_file.Classification import classification
from Load_from_file.Input_array_format import format_input

PLV5 = Preprocess(filename ,'plv','5',filter_lapl=True)
PLV6 = Preprocess(filename,'plv','6',filter_lapl=True)
PLV7 = Preprocess(filename,'plv','7',filter_lapl=True)

#PLI = Preprocess('..\Data\JohnImag1.bdf','pli')
#WPLI = Preprocess('..\Data\JohnImag1.bdf','wpli')


#Returns a 5 dimensional array
#1 - Computed connectivity measure (67 x 67 x n_freqs)
#2 - Frequency points at which the connectivity was computed
#3 - Time points for which the connectivity was computed.
#4 - Number of epochs used for computation.
#5 - The number of DPSS tapers used
input5,targets5 = format_input(PLV5,'mov_5')
input6,targets6 = format_input(PLV6,'mov_6')
input7,targets7 = format_input(PLV7,'mov_7')

input = np.concatenate((input5,input6,input7),axis = 0)
targets = np.concatenate((targets5, targets6, targets7),axis = 0 )


#sample size in percentage
classifier = classification(input,targets, sample_percentage = 40, evaluate = True)



