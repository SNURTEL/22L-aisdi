def selection_sort(array: list) -> list:
    for i in range(len(array)):
        min_j = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_j]:
                min_j = j
        if min_j != i:
            array[i], array[min_j] = array[min_j], array[i]
    return array
