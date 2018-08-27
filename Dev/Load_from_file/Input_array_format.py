import numpy as np
def format_input(input,move_type):
    input = np.array(input[0])
    input = np.delete(input, [64, 65, 66, 67], axis=0)
    input = np.delete(input,[64,65,66,67],axis = 1)
    input = np.transpose(input, [2, 0, 1])
    list_of_flat_inputs = []
    for i in range(0, len(input)):
        flat_input = input[i].flatten()
        list_of_flat_inputs.append(flat_input)
    input = np.array(list_of_flat_inputs)
    NaN_indexes = np.isnan(input)
    input[NaN_indexes] = 0

    targets = []
    for i in range(0, len(input)):
        targets.append(move_type)
    targets = np.array(targets)
    return input,targets