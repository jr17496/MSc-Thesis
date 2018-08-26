import numpy as np
#External electrode data is removed
#The format of the input array is 64x64x307, this is transposed to 307x64x64 and flattened
#307 is the amount of timesteps each window contains, while 64x64 is the connectivity between channels
#NaN values if any are replaced by 0
def format_input(input):
    input=input[0]
    input = np.array(input)
    input = np.delete(input, [64, 65, 66, 67,68,69,70,71], axis=0)
    input = np.delete(input,[64,65,66,67,68,69,70,71],axis = 1)
    input = np.transpose(input,[2,0,1])

    input = input.flatten()


    NaN_indexes = np.isnan(input)
    input[NaN_indexes] = 0
    return input