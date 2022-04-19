import random
import numpy as np

from lab04_heaps.src.maxKHeap import MaxKHeap


class ExtendedMaxKHeap(MaxKHeap):
    def validate(self, root_idx):
        if self._is_leaf(root_idx):
            return

        for child_idx in [self._get_k_child_idx(k, root_idx) for k in range(self._children_count)]:
            if self._is_leaf(child_idx):
                return

            assert self._verify_relation(root_idx, child_idx)
            self.validate(child_idx)

        return True

    def _verify_relation(self, parent_idx, child_idx):
        return self._array[parent_idx] >= self._array[child_idx]


def make_random_arrays(min_length, max_length, min_val, max_val, array_count):
    return [np.random.choice(range(min_val, max_val), size=random.randint(min_length, max_length), replace=True) for _
            in range(array_count)]
