from typing import Any, List


def bubble_sort(array: List[Any]) -> List[Any]:
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
    return array
