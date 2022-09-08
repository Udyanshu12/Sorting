def merge_list(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            combined.append(list2[j])
            j = j + 1
        else:
            combined.append(list1[i])
            i = i + 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(arr_list):
    if len(arr_list) == 1:
        return arr_list
    mid = int(len(arr_list)/2)
    left = arr_list[:mid]
    right = arr_list[mid:]
    return merge_list(merge_sort(left), merge_sort(right))

