from typing import Any, List


def insertion_sort(array: List[Any]) -> List[Any]:
    for i in range(1, len(array)):
        current = array[i]

        j = i
        while array[j-1] > current and j:
            j -= 1
        array.insert(j, array.pop(i))

    return array
