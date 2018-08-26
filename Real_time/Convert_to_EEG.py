import numpy as np
import mne

#A montage is assigned to the data, and channels are separated into eeg and eog channels

def convert (data):
    ch_names = [
        'fp1','AF7','AF3','F1','F3','F5','F7','FT7','FC5','FC3','FC1','C1','C3','C5','T7','TP7','CP5','CP3','CP1','P1','P3','P5','P7','P9','PO7','PO3','O1','IZ','OZ','POZ','PZ','CPZ',
        'Fpz','FP2','AF8','AF4','AFZ','Fz','F2','F4','F6','F8','FT8','FC6','FC4','FC2','FCz','CZ','C2','C4','C6','T8','TP8','CP6','CP4','CP2','P2','P4','P6','P8','P10','PO8','PO4','O2',
        'RPA','lpa','nz','EX4','EX5','EX6','EX7','EX8','STI 014']
    sfreq = 512

    ch_types = []

    #First 64 channels are EEG data, remaining 3 are EOG data
    for i in range(len(ch_names) - 8):
        ch_types.append('eeg')
    ch_types.append('eog')
    ch_types.append('eog')
    ch_types.append('eog')
    ch_types.append('eog')
    ch_types.append('eog')
    ch_types.append('eog')
    ch_types.append('eog')
    ch_types.append('eog')


    info = mne.create_info(ch_names, sfreq,ch_types=ch_types)

    raw = mne.io.RawArray(data, info)

    montage = mne.channels.read_montage('biosemi64')
    raw.set_montage(montage)



    return(raw)

