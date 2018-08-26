#Applies a notch, low-pass and high-pass filter to the data

def filter_data(data):
    data.notch_filter(50, filter_length='auto',
                      phase='zero')
    data.filter(None,60., fir_design='firwin')
    data.filter(5, None, fir_design='firwin')
    return data