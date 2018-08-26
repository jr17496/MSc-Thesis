import numpy as np

#laplacina filtering is applied to each timestep of the data
def laplacian(epoch):
    laplacian_filtered = []
    for i in range(0,len(epoch)):
        laplacian_filtered.append(laplacian_values(epoch))

    return(np.array(laplacian_filtered))


#The channels surrounding each channel were selected manualy and the signal value at the given timestep was averaged
#The average signal value was subtracted from the corresponding channel

def laplacian_values(epoch):
    avg_0 = (epoch[1] + epoch[2] + epoch[32])/3
    avg_1 = (epoch[0] + epoch[2] + epoch[5] + epoch[6])/4
    avg_2 = (epoch[0] + epoch[1] + epoch[4] + epoch[5] + epoch[36])/5
    avg_3 = (epoch[4] + epoch[10] + epoch[36] + epoch[37])/4
    avg_4 = (epoch[2] + epoch[3] + epoch[5] + epoch[9])/4
    avg_5 = (epoch[1] + epoch[2] + epoch[4] + epoch[6] + epoch[8])/5
    avg_6 = (epoch[1] + epoch[5] + epoch[7])/3
    avg_7 = (epoch[6] + epoch[8] + epoch[14]) / 3
    avg_8 = (epoch[5] + epoch[7] + epoch[9] + epoch[13])/4
    avg_9 = (epoch[4] + epoch[8] + epoch[10] + epoch[12]) / 4
    avg_10 = (epoch[3] + epoch[9] + epoch[11] + epoch[46]) / 4
    avg_11 = (epoch[10] + epoch[12] + epoch[18] + epoch[47]) / 4
    avg_12 = (epoch[9] + epoch[11] + epoch[13] + epoch[17]) / 4
    avg_13 = (epoch[8] + epoch[12] + epoch[14] + epoch[16]) / 4
    avg_14 = (epoch[7] + epoch[13] + epoch[15]) / 3
    avg_15 = (epoch[14] + epoch[16] + epoch[22]) / 3
    avg_16 = (epoch[13] + epoch[15] + epoch[17] + epoch[21]) / 4
    avg_17 = (epoch[12] + epoch[16] + epoch[18] + epoch[20]) / 4
    avg_18 = (epoch[11] + epoch[17] + epoch[19] + epoch[31]) / 4
    avg_19 = (epoch[18] + epoch[20] + epoch[29] + epoch[30]) / 4
    avg_20 = (epoch[17] + epoch[19] + epoch[21] + epoch[25]) / 4
    avg_21 = (epoch[16] + epoch[20] + epoch[22] + epoch[24] + epoch[25])/5
    avg_22 = (epoch[15] + epoch[21] + epoch[23] + epoch[24]) / 4
    avg_23 = (epoch[15] + epoch[22] + epoch[24]) / 3
    avg_24 = (epoch[21] + epoch[22] + epoch[23] + epoch[25] + epoch[26]) / 5
    avg_25 = (epoch[20] + epoch[24] + epoch[26] + epoch[29]) / 4
    avg_26 = (epoch[24] + epoch[25] + epoch[27] + epoch[28] + epoch[29]) / 5
    avg_27 = (epoch[26] + epoch[28] + epoch[63]) / 3
    avg_28 = (epoch[26] + epoch[27] + epoch[29] + epoch[63]) / 4
    avg_29 = (epoch[19] + epoch[25] + epoch[26] + epoch[28]+ epoch[30] + epoch[17] + epoch[62] + epoch[56]) / 8
    avg_30 = (epoch[19] + epoch[29] + epoch[31] + epoch[56]) / 4
    avg_31 = (epoch[18] + epoch[30] + epoch[47] + epoch[55]) / 4



    avg_32 = (epoch[0] + epoch[33] + epoch[36]) / 3
    avg_33 = (epoch[32] + epoch[34] + epoch[35] + epoch[36]) / 4
    avg_34 = (epoch[33] + epoch[35] + epoch[40] + epoch[41]) / 4
    avg_35 = (epoch[33] + epoch[34] + epoch[36] + epoch[38] + epoch[39] + epoch[40]) / 6
    avg_36 = (epoch[2] + epoch[3] + epoch[32] + epoch[35] + epoch[37] + epoch[38]) / 6
    avg_37 = (epoch[3] + epoch[36] + epoch[38] + epoch[42]) / 4
    avg_38 = (epoch[35] + epoch[36] + epoch[37] + epoch[39] + epoch[45]) / 5
    avg_39 = (epoch[35] + epoch[38] + epoch[40] + epoch[44]) / 4
    avg_40 = (epoch[34] + epoch[35] + epoch[39] + epoch[41] + epoch[43]) / 5
    avg_41 = (epoch[34] + epoch[40] + epoch[42]) / 3
    avg_42 = (epoch[41] + epoch[43] + epoch[51]) / 3
    avg_43 = (epoch[40] + epoch[42] + epoch[44] + epoch[50]) / 4
    avg_44 = (epoch[39] + epoch[43] + epoch[45] + epoch[49]) / 4
    avg_45 = (epoch[38] + epoch[44] + epoch[46] + epoch[48]) / 4
    avg_46 = (epoch[10] + epoch[37] + epoch[45] + epoch[47]) / 4
    avg_47 = (epoch[11] + epoch[31] + epoch[46] + epoch[48]) / 4
    avg_48 = (epoch[45] + epoch[47] + epoch[49] + epoch[55]) / 4
    avg_49 = (epoch[44] + epoch[48] + epoch[50] + epoch[54]) / 4
    avg_50 = (epoch[43] + epoch[49] + epoch[51] + epoch[53]) / 4
    avg_51 = (epoch[42] + epoch[50] + epoch[52]) / 3
    avg_52 = (epoch[51] + epoch[53] + epoch[59] + epoch[60]) / 4
    avg_53 = (epoch[50] + epoch[52] + epoch[54] + epoch[58]) / 4
    avg_54 = (epoch[49] + epoch[53] + epoch[55] + epoch[57]) / 4
    avg_55 = (epoch[31] + epoch[48] + epoch[54] + epoch[56]) / 4
    avg_56 = (epoch[29] + epoch[30] + epoch[55] + epoch[57] + epoch[62]) / 5
    avg_57 = (epoch[54] + epoch[56] + epoch[58] + epoch[62]) / 4
    avg_58 = (epoch[53] + epoch[57] + epoch[59] + epoch[61] + epoch[62]) / 5
    avg_59 = (epoch[52] + epoch[58] + epoch[60] + epoch[61]) / 4
    avg_60 = (epoch[52] + epoch[59] + epoch[61]) / 3
    avg_61 = (epoch[58] + epoch[59] + epoch[60] + epoch[62] + epoch[63]) / 5
    avg_62 = (epoch[29] + epoch[56] + epoch[57] + epoch[58] + epoch[61] + epoch[63]) / 6
    avg_63 = (epoch[27] + epoch[28] + epoch[29] + epoch[61] + epoch[62]) / 5

    epoch[0] = epoch[0] - avg_0
    epoch[1] = epoch[1] - avg_1
    epoch[2] = epoch[2] - avg_2
    epoch[3] = epoch[3] - avg_3
    epoch[4] = epoch[4] - avg_4
    epoch[5] = epoch[5] - avg_5
    epoch[6] = epoch[6] - avg_6
    epoch[7] = epoch[7] - avg_7
    epoch[8] = epoch[8] - avg_8
    epoch[9] = epoch[9] - avg_9
    epoch[10] = epoch[10] - avg_10
    epoch[11] = epoch[11] - avg_11
    epoch[12] = epoch[12] - avg_12
    epoch[13] = epoch[13] - avg_13
    epoch[14] = epoch[14] - avg_14
    epoch[15] = epoch[15] - avg_15
    epoch[16] = epoch[16] - avg_16
    epoch[17] = epoch[17] - avg_17
    epoch[18] = epoch[18] - avg_18
    epoch[19] = epoch[19] - avg_19
    epoch[20] = epoch[20] - avg_20
    epoch[21] = epoch[21] - avg_21
    epoch[22] = epoch[22] - avg_22
    epoch[23] = epoch[23] - avg_23
    epoch[24] = epoch[24] - avg_24
    epoch[25] = epoch[25] - avg_25
    epoch[26] = epoch[26] - avg_26
    epoch[27] = epoch[27] - avg_27
    epoch[28] = epoch[28] - avg_28
    epoch[29] = epoch[29] - avg_29
    epoch[30] = epoch[30] - avg_30
    epoch[31] = epoch[31] - avg_31
    epoch[32] = epoch[32] - avg_32
    epoch[33] = epoch[33] - avg_33
    epoch[34] = epoch[34] - avg_34
    epoch[35] = epoch[35] - avg_35
    epoch[36] = epoch[36] - avg_36
    epoch[37] = epoch[37] - avg_37
    epoch[38] = epoch[38] - avg_38
    epoch[39] = epoch[39] - avg_39
    epoch[40] = epoch[40] - avg_40
    epoch[41] = epoch[41] - avg_41
    epoch[42] = epoch[42] - avg_42
    epoch[43] = epoch[43] - avg_43
    epoch[44] = epoch[44] - avg_44
    epoch[45] = epoch[45] - avg_45
    epoch[46] = epoch[46] - avg_46
    epoch[47] = epoch[47] - avg_47
    epoch[48] = epoch[48] - avg_48
    epoch[49] = epoch[49] - avg_49
    epoch[50] = epoch[50] - avg_50
    epoch[51] = epoch[51] - avg_51
    epoch[52] = epoch[52] - avg_52
    epoch[53] = epoch[53] - avg_53
    epoch[54] = epoch[54] - avg_54
    epoch[55] = epoch[55] - avg_55
    epoch[56] = epoch[56] - avg_56
    epoch[57] = epoch[57] - avg_57
    epoch[58] = epoch[58] - avg_58
    epoch[59] = epoch[59] - avg_59
    epoch[60] = epoch[60] - avg_60
    epoch[61] = epoch[61] - avg_61
    epoch[62] = epoch[62] - avg_62
    epoch[63] = epoch[63] - avg_63

    return(epoch)