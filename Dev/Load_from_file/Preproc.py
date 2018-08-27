import numpy as np
import mne
from Load_from_file.Convert_to_EEG_load import convert
from Load_from_file.Filter_data import filter_data
from Laplacian_filter import laplacian
from Load_from_file.Input_array_format import format_input
from Load_from_file.spatial_filter import spatial_filter
from mne.decoding import EMS, compute_ems


def Preprocess(file_name,metric='plv',event_id = '5',filter_lapl = False):
    raw = mne.io.read_raw_edf(file_name, preload=True)
    raw.drop_channels(['EXG4','EXG5','EXG6','EXG7','EXG8'])


    raw = convert(raw)
    raw = filter_data(raw)

    if filter_lapl == False:
        #rereference using RPA
        #raw[0] rereferenced array
        #raw[1] Array of reference data subtracted from EEG channels
        raw = mne.set_eeg_reference(raw,['RPA'])
        raw = raw[0]
    event_index = event_id


    #stimulus codes will require change
    events = mne.find_events(raw, stim_channel='STI 014', verbose=False, initial_event=True)
    #print('Unique event codes:', np.unique(events[:, 2]))
    event_id = {'1': 65282, '2': 65284, '3': 65288, '4': 65296, '5': 65344, '6': 65408, '7': 65472, '8': 130816}

    picks = mne.pick_types(raw.info, meg=False, eeg=True, stim=False, eog=True,
                           exclude='bads')
    epochs = mne.Epochs(raw, events, event_id, tmin=0, tmax=0.6 ,picks = picks,baseline=None, preload=True, reject = dict(eog=150e-6), reject_by_annotation=True)

    lapl_filtered = []

    if filter_lapl == True:
        for ep in epochs['5']:
            ep = (laplacian((ep)))
            print(len(ep))


    #spatial filtering needs to be improved on and change epochs[event_index] in classification_inputs when completed
    #epochs = spatial_filter(raw, epochs[event_index])
    classification_inputs = mne.connectivity.spectral_connectivity(epochs[event_index], method=metric)
    return classification_inputs




