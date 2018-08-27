from mne.preprocessing import Xdawn
from mne import compute_raw_covariance, pick_types
def spatial_filter(raw, epochs):
    print('spatial filtering using xDawn')
    picks = pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False,exclude='bads')
    signal_cov = compute_raw_covariance(raw, picks=picks)
    xd = Xdawn(n_components=2, signal_cov=signal_cov)
    print('fiting xDawn')
    xd.fit(epochs)
    print('epoch denoising started')
    epochs_denoised = xd.apply(epochs)
    print('epoch_denoise complete')
    return epochs_denoised