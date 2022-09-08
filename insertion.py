def insertion_sort(arr_list):
    for i in range(1, len(arr_list)):
        j = i - 1
        temp = arr_list[i]
        while arr_list[j] > temp and j > -1:
            arr_list[j + 1] = arr_list[j]
            arr_list[j] = temp
            j = j - 1
    return arr_list
