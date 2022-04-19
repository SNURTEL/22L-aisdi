from abc import ABC, abstractmethod
from typing import Sequence


class HeapError(Exception):
    def __init__(self, msg: str = ''):
        super(HeapError, self).__init__(msg)


class Heap(ABC):
    def __init__(self, array: Sequence = None):
        self._array = []
        if array is not None:
            self._create_heap(list(array))

    @abstractmethod
    def insert(self, element):
        pass

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def _create_heap(self, array: Sequence):
        pass
