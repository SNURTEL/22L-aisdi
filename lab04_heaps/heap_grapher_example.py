from lab04_heaps.src.maxKHeap import MaxKHeap
from lab04_heaps.util.heap_grapher import HeapGrapher


if __name__ == '__main__':
    import random

    h = MaxKHeap(4, random.sample(range(0, 10000), 100))

    hg = HeapGrapher()
    hg.graph_tree(h)
    pass
