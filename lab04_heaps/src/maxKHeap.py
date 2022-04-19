from lab04_heaps.src.heap import Heap
from typing import Sequence


class MaxKHeap(Heap):
    def __init__(self, children_count: int, array: Sequence = None):
        self._children_count = children_count
        super(MaxKHeap, self).__init__(array)

    @property
    def array(self):
        return self._array

    def _create_heap(self, array: list):
        self._array = array
        for i in range(len(self._array) // self._children_count - 1, -1, -1):
            self._heapify(i)

    def _heapify(self, idx: int):
        if self._is_leaf(idx):
            return
        # # TODO
        # lchild_idx = self._get_lchild_idx(idx)
        # rchild_idx = self._get_rchild_idx(idx)
        #
        # if rchild_idx >= len(self._array):  # rchild does not exist
        #     if self._array[idx] < self._array[lchild_idx]:
        #         self._swap(idx, lchild_idx)
        #     return
        #
        # if self._array[idx] < self._array[lchild_idx] or self._array[idx] < self._array[rchild_idx]:
        #     if self._array[lchild_idx] > self._array[rchild_idx]:
        #         self._swap(idx, lchild_idx)
        #         self._heapify(lchild_idx)
        #     else:
        #         self._swap(idx, rchild_idx)
        #         self._heapify(rchild_idx)

        children = self.get_all_children(idx)
        if not self._array[idx] > max(children):
            max_child_idx = children.index(max(children))
            self._swap(idx, self._get_k_child_idx(max_child_idx, idx))
            self._heapify(self._get_k_child_idx(max_child_idx, idx))

    def _is_leaf(self, idx):
        return idx * self._children_count >= len(self._array) - 1  # if leaf

    def get_all_children(self, idx):
        return self._array[min(idx * self._children_count + 1, len(self._array)): min((idx + 1) * self._children_count + 1,
                                                                                      len(self._array))]

    def _get_k_child_idx(self, k, idx):
        return self._children_count * idx + k + 1

    def _get_parent_idx(self, idx):
        return max((idx - 1) // self._children_count, 0)  # return 0 if trying to get root's parent

    def _swap(self, idx1, idx2):
        print(f"Input array: {self._array}")
        self._array[idx1], self._array[idx2] = self._array[idx2], self._array[idx1]
        print(f"Swapped {self._array[idx1]} with {self._array[idx2]}\nResult array: {self._array}\n")

    def insert(self, element):  # move to base class?
        current_idx = len(self._array)
        parent_idx = self._get_parent_idx(current_idx)
        self._array.append(element)

        while element > self._array[parent_idx]:
            self._swap(current_idx, parent_idx)
            current_idx = parent_idx
            parent_idx = self._get_parent_idx(parent_idx)

    def extract(self):
        self._array[0] = self._array.pop()
        self._heapify(0)


if __name__ == '__main__':
    print([17, 1, 2, 19, 7, 100, 36, 25, 3], '\n')

    h = MaxKHeap(3, [17, 1, 2, 19, 7, 100, 36, 25, 3])
    print(h.array)

    # h.insert(47)
    #
    # print("Insert 47:\n", h.array)
    #
    # h.extract()
    #
    # print("Extract:\n", h.array)
