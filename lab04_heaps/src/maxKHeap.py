from lab04_heaps.src.heap import Heap, HeapError
from typing import Sequence


class MaxKHeap(Heap):
    def __init__(self, children_count: int, array: Sequence = None):
        if not children_count:
            raise HeapError("Children count cannot be 0")

        self._children_count = children_count
        super(MaxKHeap, self).__init__(array)

    @property
    def array(self):
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
            self._swap(idx, self._get_k_child_idx(max_child_idx, idx))
            self._heapify(self._get_k_child_idx(max_child_idx, idx))

    def _is_leaf(self, idx):
        return idx * self._children_count >= len(self._array) - 1  # if leaf

    def get_all_children(self, idx):
        return self._array[
               min(idx * self._children_count + 1, len(self._array)): min((idx + 1) * self._children_count + 1,
                                                                          len(self._array))]

    def _get_k_child_idx(self, k, idx):
        return self._children_count * idx + k + 1

    def _get_parent_idx(self, idx):
        return max((idx - 1) // self._children_count, 0)  # return 0 if trying to get root's parent

    def _swap(self, idx1, idx2):
        self._array[idx1], self._array[idx2] = self._array[idx2], self._array[idx1]

    def insert(self, element):  # move to base class?
        current_idx = len(self._array)
        parent_idx = self._get_parent_idx(current_idx)
        self._array.append(element)

        while element > self._array[parent_idx]:
            self._swap(current_idx, parent_idx)
            current_idx = parent_idx
            parent_idx = self._get_parent_idx(parent_idx)

    def extract(self):
        if len(self._array) == 0:
            raise HeapError("Cannot extract root element from an empty heap")
        elif len(self._array) == 1:
            return self._array.pop()

        root = self._array[0]
        self._array[0] = self._array.pop()
        self._heapify(0)
        return root
