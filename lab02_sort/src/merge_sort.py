from typing import Any, List


def merge_sort(array: List[Any]) -> List[Any]:
    if len(array) == 1:
        return array
    div_point = floor(len(array)/2)
    first_partition = array[:div_point]
    second_partition = array[div_point:]
    sorted_first_partition = merge_sort(first_partition)
    sorted_second_partition = merge_sort(second_partition)
    if first_partition[0] > second_partition[0]:
        return sorted_second_partition.extend(sorted_first_partition)
    else:
        return sorted_first_partition.extend(sorted_second_partition)
