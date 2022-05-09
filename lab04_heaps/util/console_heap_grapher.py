import enum
from io import StringIO
import math
from lab04_heaps.src.maxKHeap import MaxKHeap


class ConsoleHeapGrapher:
    def __init__(self):
        self._buffer = StringIO()
        self._total_width = 60  # maybe generate based on contents?
        self._fill_char = " "

    def graph_tree(self, tree: MaxKHeap):
        self._raw_data = tree.get_raw_data()
        self._num_children = tree.num_children
        self._write_tree()
        self._print_buffer()

    def _get_row_from_idx(self, idx):
        if idx:
            return int(math.floor(math.log(idx+1, self._num_children)))
        else:
            return 0

    def _write_tree(self):
        last_row = 0
        for i, n in enumerate(self._raw_data):
            row = self._get_row_from_idx(i)
            if row != last_row:
                self._buffer.write("\n")
            n_columns = self._num_children**row
            col_width = int(math.floor((self._total_width * 1.0) / n_columns))
            self._write_col_data(col_width, n)
            last_row = row

    def _write_col_data(self, col_width, n):
        self._buffer.write(str(n).center(col_width, self._fill_char))

    def _print_buffer(self):
        print(self._buffer.getvalue())
