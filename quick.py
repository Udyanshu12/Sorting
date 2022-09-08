def swap(arr_list, index1, index2):
    temp = arr_list[index1]
    arr_list[index1] = arr_list[index2]
    arr_list[index2] = temp


def pivot(arr_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if arr_list[pivot_index] > arr_list[i]:
            swap_index += 1
            swap(arr_list, swap_index, i)
    swap(arr_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(arr_list, left, right):
    if left < right:
        pivot_index = pivot(arr_list, left, right)
        quick_sort_helper(arr_list, left, pivot_index - 1)
        quick_sort_helper(arr_list, pivot_index + 1, right)
    return arr_list


def quick_sort(arr_list):
    return quick_sort_helper(arr_list, 0, len(arr_list) - 1)
