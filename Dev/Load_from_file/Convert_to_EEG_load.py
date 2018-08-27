import numpy as np
import mne

def convert (raw):
    # Rename channels
    raw.info['chs'][raw.ch_names.index('A1')]['ch_name'] = 'fp1'
    raw.info['chs'][raw.ch_names.index('A2')]['ch_name'] = 'AF7'
    raw.info['chs'][raw.ch_names.index('A3')]['ch_name'] = 'AF3'
    raw.info['chs'][raw.ch_names.index('A4')]['ch_name'] = 'F1'
    raw.info['chs'][raw.ch_names.index('A5')]['ch_name'] = 'F3'
    raw.info['chs'][raw.ch_names.index('A6')]['ch_name'] = 'F5'
    raw.info['chs'][raw.ch_names.index('A7')]['ch_name'] = 'F7'
    raw.info['chs'][raw.ch_names.index('A8')]['ch_name'] = 'FT7'
    raw.info['chs'][raw.ch_names.index('A9')]['ch_name'] = 'FC5'
    raw.info['chs'][raw.ch_names.index('A10')]['ch_name'] = 'FC3'
    raw.info['chs'][raw.ch_names.index('A11')]['ch_name'] = 'FC1'
    raw.info['chs'][raw.ch_names.index('A12')]['ch_name'] = 'C1'
    raw.info['chs'][raw.ch_names.index('A13')]['ch_name'] = 'C3'
    raw.info['chs'][raw.ch_names.index('A14')]['ch_name'] = 'C5'
    raw.info['chs'][raw.ch_names.index('A15')]['ch_name'] = 'T7'
    raw.info['chs'][raw.ch_names.index('A16')]['ch_name'] = 'TP7'
    raw.info['chs'][raw.ch_names.index('A17')]['ch_name'] = 'CP5'
    raw.info['chs'][raw.ch_names.index('A18')]['ch_name'] = 'CP3'
    raw.info['chs'][raw.ch_names.index('A19')]['ch_name'] = 'CP1'
    raw.info['chs'][raw.ch_names.index('A20')]['ch_name'] = 'P1'
    raw.info['chs'][raw.ch_names.index('A21')]['ch_name'] = 'P3'
    raw.info['chs'][raw.ch_names.index('A22')]['ch_name'] = 'P5'
    raw.info['chs'][raw.ch_names.index('A23')]['ch_name'] = 'P7'
    raw.info['chs'][raw.ch_names.index('A24')]['ch_name'] = 'P9'
    raw.info['chs'][raw.ch_names.index('A25')]['ch_name'] = 'PO7'
    raw.info['chs'][raw.ch_names.index('A26')]['ch_name'] = 'PO3'
    raw.info['chs'][raw.ch_names.index('A27')]['ch_name'] = 'O1'
    raw.info['chs'][raw.ch_names.index('A28')]['ch_name'] = 'IZ'
    raw.info['chs'][raw.ch_names.index('A29')]['ch_name'] = 'OZ'
    raw.info['chs'][raw.ch_names.index('A30')]['ch_name'] = 'POZ'
    raw.info['chs'][raw.ch_names.index('A31')]['ch_name'] = 'PZ'
    raw.info['chs'][raw.ch_names.index('A32')]['ch_name'] = 'CPZ'

    raw.info['chs'][raw.ch_names.index('B1')]['ch_name'] = 'Fpz'
    raw.info['chs'][raw.ch_names.index('B2')]['ch_name'] = 'FP2'
    raw.info['chs'][raw.ch_names.index('B3')]['ch_name'] = 'AF8'
    raw.info['chs'][raw.ch_names.index('B4')]['ch_name'] = 'AF4'
    raw.info['chs'][raw.ch_names.index('B5')]['ch_name'] = 'AFZ'
    raw.info['chs'][raw.ch_names.index('B6')]['ch_name'] = 'Fz'
    raw.info['chs'][raw.ch_names.index('B7')]['ch_name'] = 'F2'
    raw.info['chs'][raw.ch_names.index('B8')]['ch_name'] = 'F4'
    raw.info['chs'][raw.ch_names.index('B9')]['ch_name'] = 'F6'
    raw.info['chs'][raw.ch_names.index('B10')]['ch_name'] = 'F8'
    raw.info['chs'][raw.ch_names.index('B11')]['ch_name'] = 'FT8'
    raw.info['chs'][raw.ch_names.index('B12')]['ch_name'] = 'FC6'
    raw.info['chs'][raw.ch_names.index('B13')]['ch_name'] = 'FC4'
    raw.info['chs'][raw.ch_names.index('B14')]['ch_name'] = 'FC2'
    raw.info['chs'][raw.ch_names.index('B15')]['ch_name'] = 'FCz'
    raw.info['chs'][raw.ch_names.index('B16')]['ch_name'] = 'CZ'
    raw.info['chs'][raw.ch_names.index('B17')]['ch_name'] = 'C2'
    raw.info['chs'][raw.ch_names.index('B18')]['ch_name'] = 'C4'
    raw.info['chs'][raw.ch_names.index('B19')]['ch_name'] = 'C6'
    raw.info['chs'][raw.ch_names.index('B20')]['ch_name'] = 'T8'
    raw.info['chs'][raw.ch_names.index('B21')]['ch_name'] = 'TP8'
    raw.info['chs'][raw.ch_names.index('B22')]['ch_name'] = 'CP6'
    raw.info['chs'][raw.ch_names.index('B23')]['ch_name'] = 'CP4'
    raw.info['chs'][raw.ch_names.index('B24')]['ch_name'] = 'CP2'
    raw.info['chs'][raw.ch_names.index('B25')]['ch_name'] = 'P2'
    raw.info['chs'][raw.ch_names.index('B26')]['ch_name'] = 'P4'
    raw.info['chs'][raw.ch_names.index('B27')]['ch_name'] = 'P6'
    raw.info['chs'][raw.ch_names.index('B28')]['ch_name'] = 'P8'
    raw.info['chs'][raw.ch_names.index('B29')]['ch_name'] = 'P10'
    raw.info['chs'][raw.ch_names.index('B30')]['ch_name'] = 'PO8'
    raw.info['chs'][raw.ch_names.index('B31')]['ch_name'] = 'PO4'
    raw.info['chs'][raw.ch_names.index('B32')]['ch_name'] = 'O2'

    raw.info['chs'][raw.ch_names.index('EXG1')]['ch_name'] = 'RPA'
    raw.info['chs'][raw.ch_names.index('EXG2')]['ch_name'] = 'lpa'
    raw.info['chs'][raw.ch_names.index('EXG3')]['ch_name'] = 'nz'


    ch_names = [
        'fp1','AF7','AF3','F1','F3','F5','F7','FT7','FC5','FC3','FC1','C1','C3','C5','T7','TP7','CP5','CP3','CP1','P1','P3','P5','P7','P9','PO7','PO3','O1','IZ','OZ','POZ','PZ','CPZ',
        'Fpz','FP2','AF8','AF4','AFZ','Fz','F2','F4','F6','F8','FT8','FC6','FC4','FC2','FCz','CZ','C2','C4','C6','T8','TP8','CP6','CP4','CP2','P2','P4','P6','P8','P10','PO8','PO4','O2',
        'RPA','lpa','nz']

    for i in range(0,len(ch_names)):
        raw.info['ch_names'][i] = ch_names[i]

    montage = mne.channels.read_montage('biosemi64')
    raw.set_montage(montage)

    raw.set_channel_types(mapping={'RPA': 'eog'})
    raw.set_channel_types(mapping={'lpa': 'eog'})
    raw.set_channel_types(mapping={'nz': 'eog'})



    return(raw)

