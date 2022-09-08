def selection_sort(arr_list):
    for i in range(len(arr_list)):
        min_index = i
        for j in range(i + 1, len(arr_list)):
            if arr_list[min_index] > arr_list[j]:
                min_index = j
        if min_index != i:
            temp = arr_list[i]
            arr_list[i] = arr_list[min_index]
            arr_list[min_index] = temp
    return arr_list
