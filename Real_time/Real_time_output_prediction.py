import datetime
from Real_time.Convert_to_EEG import convert
from Real_time.Filter_data import filter_data
from Real_time.Input_array_format_real_time import format_input
from Laplacian_filter import laplacian
import numpy as np
from pylsl import StreamInlet, resolve_stream
import mne
import pickle
from pyautogui import press,click


filter_lapl = True
prev_time = 0
classification_segment = []

streams = resolve_stream('type', 'EEG')
inlet = StreamInlet(streams[0])

#The data is collected continuously for a time period of 1 second (512 timesteps)
#at the start of each collected data segment a stimulus value of 1 is added to an artificial stimulus channel used for epoching
#the data is preprocessed in the same way as it was when training the classifier with a difference that the epoching is performed using
#a stimulus code of 1, if epoching was unsuccessful due to too few timesteps recorded the next sample is processed

while True:
    sample, timestamp = inlet.pull_sample()
    # timestamp transformed into seconds
    current_time = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
    # print(current_time, sample)
    if current_time == prev_time:
        classification_segment.append(sample)
    else:
        if len(classification_segment)> 0:
            data = np.array(classification_segment)
            data= np.transpose(data)
            #changed first data samples stimulus value to 1 to indicate the start of the epoch
            data[72][0] = 1.
            print(data[72][0])
            data = convert(data)
            data = filter_data(data)
            if filter_lapl == False:
                raw = mne.set_eeg_reference(raw, ['RPA'])
                raw = raw[0]
            #############
            events = mne.find_events(data, stim_channel='STI 014', verbose=False, initial_event=True)
            event_id = {'1': 1}

            epochs = mne.Epochs(data, events, event_id, tmin=0, tmax=0.6,
                                baseline=None, preload=True)


            if filter_lapl == True:
                for ep in epochs:
                    lapl_filtered= (laplacian((ep)))
                    ep = lapl_filtered
                    print('Start of new one')

            try:
                PLV = mne.connectivity.spectral_connectivity(epochs['1'], method='plv')
                input =format_input(PLV)
                input = input.reshape(1,-1)


                #The pretrained classifier is loaded and used to predict using the preprocessed data

                clf = pickle.load(open( '..\Real_time\SVM_classifierPLV.pkl', "rb" ))

                prediction = clf.predict(input)

                #Predicted outputs are matched to keyboard inputs

                print(prediction)
                if prediction[0] == 'Left':
                    print('Left')
                    press('left',interval = 0.2)
                elif prediction[0] =='Right':
                    print('Right')
                    press('right', interval=0.2)
                elif prediction[0] == 'Up':
                    print('Up')
                    press('up', interval=0.2)
                elif prediction[0] == 'Down':
                    print('Down')
                    press('down', interval=0.2)
                elif prediction[0] == 'Tongue':
                    print('Tongue')
                    press('space', interval=0.2)
                elif prediction[0] == 'Idle':
                    print('Idle')

            except:
                print('Sync')
                pass

        classification_segment = []