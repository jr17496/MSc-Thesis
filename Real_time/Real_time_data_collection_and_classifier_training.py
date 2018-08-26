import datetime
from Real_time.Convert_to_EEG import convert
from Real_time.Filter_data import filter_data
from Real_time.Input_array_format_real_time import format_input
from Laplacian_filter import laplacian
import numpy as np
from pylsl import StreamInlet, resolve_stream
import mne
from Classification import classification
import pandas as pd


filter_lapl = True
prev_time = 0
classification_segment = []
collected_data = []
target_list = []

#provides an alternative stoping criterion to using the end of session stimulus
number_of_trials = 10000


streams = resolve_stream('type', 'EEG')
inlet = StreamInlet(streams[0])
sample_flag = False
data_collection_flag = True
Final_input_matrix_PLV = []
Final_input_matrix_PLI = []
laplacian_filtered_only = []


#data is collected till the number of trials has not been reached or the end of session stimulus has been recieved
#sample data is recorded between the start of trial and end of trial stimulus
#a list is created using the stimuluses coresponding to images to provide classification targets

while data_collection_flag == True:
    sample, timestamp = inlet.pull_sample()

    if(sample[72]!=0):
        print(sample[72])
        #768 start of trial
        #780 - arrow up
        #769 - left hand
        #772 - Tongue
        #770- right hand
        #774 - arrow down
        #33041 - idle
        #800 - end of trial
        #1010 - end of session



    if(sample[72]==768):
        sample_flag = True
        classification_segment.append(sample)

    if(sample[72] == 800):
        sample_flag = False
    if (sample_flag == True):
        classification_segment.append(sample)

    if (sample[72]==780):
        target_list.append('Up')
    elif (sample[72] == 769):
        target_list.append('Left')
    elif (sample[72]==770):
        target_list.append('Right')
    elif (sample[72]==774):
        target_list.append('Down')
    elif (sample[72]==772):
        target_list.append('Tongue')
    elif (sample[72] == 33041):
        target_list.append('Idle')

    if(sample_flag == False) and (len(classification_segment)>0):
        collected_data.append(classification_segment)
        classification_segment = []

    if(len(collected_data)== number_of_trials):
        data_collection_flag = False
    if(sample[72] == 1010):
        data_collection_flag = False


#Data could be saved to a pickle object at this point, but was commented out to make the process faster

#collected_data_df = pd.DataFrame(collected_data)
#collected_data_df.to_pickle('Raw_data.pkl')





for data in collected_data:
    # Each trial is assigned a montage and notch and band pass filtered
    data = np.array(data)
    data = np.transpose(data)
    data = convert(data)
    data = filter_data(data)
    # If Laplacian filtering was not used the external RPA electrode will be used to reference the data
    if filter_lapl == False:
        raw = mne.set_eeg_reference(raw, ['RPA'])
        raw = raw[0]
    #events maps the timestep to corresponding stimulus codes
    events = mne.find_events(data, stim_channel='STI 014', verbose=False, initial_event=False)
    print('Unique event codes:', np.unique(events[:, 2]))
    event_id = {'33040': 33040}
    # epoching is performed using a uniform 33040 stimulus code which occurs 0.2 sec after the visual stimulus disappears for 600 ms
    # the mne.Epoching function provides the functionality of artefact removal but was not used to avoid a disbalanced dataset
    epochs = mne.Epochs(data, events, event_id, tmin=0.4, tmax=1,
                            baseline=None, preload=True)
    # laplacian filtering is applied at this point if enabled
    if filter_lapl == True:
        for ep in epochs:
            lapl_filtered = (laplacian((ep)))
            ep = lapl_filtered
            laplacian_filtered_only.append(lapl_filtered)

    # the PLV and PLI connectivity metrics are calculated for all epoch corresponding to the uniform stimulus
    PLV = mne.connectivity.spectral_connectivity(epochs['33040'], method='plv')
    PLI = mne.connectivity.spectral_connectivity(epochs['33040'], method='pli')

    input_PLV = format_input(PLV)
    Final_input_matrix_PLV.append(input_PLV)

    input_PLI = format_input(PLI)
    Final_input_matrix_PLI.append(input_PLI)

    print('FINISHED WITH 1 DATA SEGMENT')
print('Done')


#Transformes the filter signals into a input useable by the classifier
#This was explored as an alternative feature to connectivity metrics

Classification_input_formated_only = np.array(laplacian_filtered_only)
Classification_input_formated_only = np.delete(Classification_input_formated_only, [64,65,66,67,68,69,70,71,72], 1)
Classification_input_formated_only = np.delete(Classification_input_formated_only, [64,65,66,67,68,69,70,71,72], 2)

Classification_input_formated_only = Classification_input_formated_only.reshape(30,1261568)



Classification_input_PLV = np.array(Final_input_matrix_PLV)
Classification_input_PLI = np.array(Final_input_matrix_PLI)


Classification_targets = np.array(target_list)



#The preprocesed data can be saved to a file as well as the targets but was commented out to make the process faster

#np.savetxt("Preprocessed_data.csv", Classification_input_PLV, delimiter=",")
#############################
#target_file =  open("Targets.csv","w")
#for item in Classification_targets:
#    target_file.write("%s," % item)


#Three classifiers for each metric are trained and evaluated on 30% of the training set before training them on the entire training set
#a method is called containing the full training set for a metric, targets, sample percentage, a flag to perform evaluation or not
#as well as the classifier to be used and which metric was used( the name of metric and the name of the classifier are used to
#name the serialized classifier object files)


print('\n\n')
print('Classifier training using PLV')
print('SVM')
classification(Classification_input_PLV,Classification_targets,sample_percentage=30,evaluate=True)
print('KNN, K = 3')
classification(Classification_input_PLV,Classification_targets,sample_percentage=30,evaluate=True,classifier = 'KNN' )
print('Random forest classifier, 10 classifiers')
classification(Classification_input_PLV,Classification_targets,sample_percentage=30,evaluate=True, classifier = 'RFC')

print('\n\n')
print('Classifier training using PLV')
print('SVM')
classification(Classification_input_PLI,Classification_targets,sample_percentage=30,evaluate=True,metric_name = 'PLI')
print('KNN, K = 3')
classification(Classification_input_PLI,Classification_targets,sample_percentage=30,evaluate=True,classifier = 'KNN', metric_name  = 'PLI' )
print('Random forest classifier, 10 classifiers')
classification(Classification_input_PLI,Classification_targets,sample_percentage=30,evaluate=True, classifier = 'RFC', metric_name  = 'PLI')



print('\n\n')
print('Classifier trained using only filtered data')
print('SVM')
classification(Classification_input_formated_only,Classification_targets,sample_percentage=30,evaluate=True,metric_name = 'filtered_only')
print('KNN, K = 3')
classification(Classification_input_formated_only,Classification_targets,sample_percentage=30,evaluate=True,classifier = 'KNN', metric_name  = 'filtered_only' )
print('Random forest classifier, 10 classifiers')
classification(Classification_input_formated_only,Classification_targets,sample_percentage=30,evaluate=True, classifier = 'RFC', metric_name  = 'filtered_only')
