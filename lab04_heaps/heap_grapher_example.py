from lab04_heaps.src.maxKHeap import MaxKHeap
from lab04_heaps.util.console_heap_grapher import ConsoleHeapGrapher


if __name__ == '__main__':
    import random

    h = MaxKHeap(2, random.sample(range(0, 100), 10))

    hg = ConsoleHeapGrapher()
    hg.graph_tree(h)
    pass
