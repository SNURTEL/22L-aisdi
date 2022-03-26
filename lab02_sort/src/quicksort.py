from typing import Any, List


def quicksort(array: List[Any], start=0, end=None) -> List[Any]:
    if len(array) < 2:
        return array

    if end is None:
        end = len(array) - 1
    current_left = start
    current_right = end

    pivot_val = array[(start + end) // 2]

    while current_left <= current_right:

        while array[current_left] < pivot_val:
            current_left += 1
        while array[current_right] > pivot_val:
            current_right -= 1

        if current_left <= current_right:
            array[current_left], array[current_right] = array[current_right], array[current_left]
            current_left += 1
            current_right -= 1

    if start < current_right:
        quicksort(array, start, current_right)
    if end > current_left:
        quicksort(array, current_left, end)

    return array
