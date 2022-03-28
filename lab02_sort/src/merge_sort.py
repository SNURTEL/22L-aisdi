from typing import Any, List


def merge_sort(array: List[Any]) -> List[Any]:
    if len(array) <= 1:
        return array

    div_point = len(array)//2

    first_part_sorted = merge_sort(array[:div_point])
    second_part_sorted = merge_sort(array[div_point:])

    return merge(first_part_sorted, second_part_sorted)


def merge(first_part: List[Any], second_part: List[Any]):
    result = []
    while len(first_part) > 0 and len(second_part) > 0:
        if(first_part[0] > second_part[0]):
            result.append(second_part.pop(0))
        else:
            result.append(first_part.pop(0))
    result.extend(first_part)
    result.extend(second_part)
    return result
