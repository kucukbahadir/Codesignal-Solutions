def rotateImage(a):
    temp_arr, const_index, arr_lengt = [x[:] for x in a], 0, len(a)
    
    for i in (range(arr_lengt)):
        for k in range(arr_lengt):
            temp_arr[const_index][k] = a[arr_lengt - k -1][const_index]

        const_index += 1

    return temp_arr