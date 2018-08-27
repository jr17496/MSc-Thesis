import numpy as np
from sklearn.decomposition import FastICA

class ICA:
    def ica(data_signals, ref_signal, verbose=False):
        data = data_signals
        reference = ref_signal
        result = []
        for i in range(len(data)):
            temp = ICA.ica_trial(data,reference)
            result.append(temp)
        return result

    @staticmethod
    def ica_trial(data_signal_trial, ref_signal_trial):
        result_trial = []
        for i in range(0,len(data_signal_trial)):
            temp = ICA.ica_sample(data_signal_trial[i],ref_signal_trial[i])
            result_trial.append(temp)
        return result_trial



    @staticmethod
    def ica_sample(data_signal_sample,ref_signal_sample):
        dat = np.array(data_signal_sample)
        ref = np.array(ref_signal_sample[0])

        data_concatenated = np.concatenate((dat[0],dat[1],ref),axis=0)

        trial_results = []
        data_concatenated /= data_concatenated.std(axis=0)
        A = np.array([[0.5, 1], [1, 0.5]])
        X = np.dot(data_concatenated.T, A.T)
        ica = FastICA(n_components=65)
        S_ = ica.fit(X)
        A_ = ica.mixing_
        return S_

