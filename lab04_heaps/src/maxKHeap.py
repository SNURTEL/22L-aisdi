from lab04_heaps.src.heap import AbstractHeap, HeapError, C
from typing import List


class MaxKHeap(AbstractHeap):
    def __init__(self, num_children: int, array: List[C] = None):
        if not num_children:
            raise HeapError("Children count cannot be 0")

        self._children_count = num_children

        if array is None:
            self._array = []
        else:
            self._create_heap(array.copy())

        super(MaxKHeap, self).__init__(num_children)  # does nothing

    def get_raw_data(self):
        return self._array

    def _create_heap(self, array: list):
        self._array = array
        for i in range(len(self._array) // self._children_count, -1, -1):
            self._heapify(i)

    def _heapify(self, idx: int):
        if self._is_leaf(idx):
            return

        children = self.get_all_children(idx)
        if not self._array[idx] > max(children):
            max_child_idx = children.index(max(children))
            self._swap(idx, self._get_kth_child_idx(max_child_idx, idx))
            self._heapify(self._get_kth_child_idx(max_child_idx, idx))

    def _is_leaf(self, idx):
        return idx * self._children_count >= len(self._array) - 1  # if leaf

    def get_all_children(self, idx):
        return self._array[
               min(idx * self._children_count + 1, len(self._array)): min((idx + 1) * self._children_count + 1,
                                                                          len(self._array))]

    def _get_kth_child_idx(self, k, idx):
        return self._children_count * idx + k + 1

    def _get_parent_idx(self, idx):
        return max((idx - 1) // self._children_count, 0)  # return 0 if trying to get root's parent

    def _swap(self, idx1, idx2):
        self._array[idx1], self._array[idx2] = self._array[idx2], self._array[idx1]

    def push(self, element):
        current_idx = len(self._array)
        parent_idx = self._get_parent_idx(current_idx)
        self._array.append(element)

        while element > self._array[parent_idx]:
            self._swap(current_idx, parent_idx)
            current_idx = parent_idx
            parent_idx = self._get_parent_idx(parent_idx)

    def pop(self):
        if len(self._array) == 0:
            raise HeapError("Cannot pop root element from an empty heap")
        elif len(self._array) == 1:
            return self._array.pop()

        root = self._array[0]
        self._array[0] = self._array.pop()
        self._heapify(0)
        return root

    def peek(self) -> C:
        return self._array[0]
