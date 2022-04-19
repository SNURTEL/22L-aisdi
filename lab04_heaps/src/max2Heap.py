from lab04_heaps.src.heap import Heap


class Max2Heap(Heap):
    @property
    def array(self):
        return self._array

    def _create_heap(self, array: list):
        self._array = array
        for i in range(len(self._array) // 2 - 1, -1, -1):
            self._heapify(i)

    def _heapify(self, idx: int):
        if idx * 2 >= len(self._array) - 1:  # if leaf
            return

        lchild_idx = self._get_lchild_idx(idx)
        rchild_idx = self._get_rchild_idx(idx)

        if rchild_idx >= len(self._array):  # rchild does not exist
            if self._array[idx] < self._array[lchild_idx]:
                self._swap(idx, lchild_idx)
            return

        if self._array[idx] < self._array[lchild_idx] or self._array[idx] < self._array[rchild_idx]:
            if self._array[lchild_idx] > self._array[rchild_idx]:
                self._swap(idx, lchild_idx)
                self._heapify(lchild_idx)
            else:
                self._swap(idx, rchild_idx)
                self._heapify(rchild_idx)

    @staticmethod
    def _get_lchild_idx(idx):
        return 2 * idx + 1

    @staticmethod
    def _get_rchild_idx(idx):
        return 2 * idx + 2

    @staticmethod
    def _get_parent_idx(idx):
        return max((idx - 1) // 2, 0)  # return 0 if trying to get root's parent

    def _rchild_exists(self, idx):
        return self._get_rchild_idx(idx) < len(self._array)

    def _swap(self, idx1, idx2):
        self._array[idx1], self._array[idx2] = self._array[idx2], self._array[idx1]

    def insert(self, element):
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
    h = Max2Heap([17, 1, 2, 19, 7, 100, 36, 25, 3])
    print(h.array)

    h.insert(47)

    print(h.array)

    h.extract()

    print(h.array)
