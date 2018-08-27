
def filter_data(data):
    #might require removing
    data.notch_filter(50, filter_length='auto',
                      phase='zero')
    data.filter(None, 50., fir_design='firwin')
    data.filter(0.5, 1, fir_design='firwin')
    return data