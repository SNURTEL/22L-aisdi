def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        current = array[i]

        j = i
        while array[j-1] > current and j:
            j -= 1
        array.insert(j, array.pop(i))

    return array
