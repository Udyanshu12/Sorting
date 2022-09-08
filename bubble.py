def bubble_sort(arr_list):
    for i in range(len(arr_list) - 1, 0, -1):
        for j in range(i):
            if arr_list[j] > arr_list[j + 1]:
                temp = arr_list[j]
                arr_list[j] = arr_list[j + 1]
                arr_list[j + 1] = temp
    return arr_list
