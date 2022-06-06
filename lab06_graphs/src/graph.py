from typing import Dict, Tuple
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


class Graph:
    def __init__(self, weights: Dict[Tuple[int, int], int], width, height):
        self.weights = weights
        self.width = width
        self.height = height

    def _find_source_dest(self):
        self.source = None
        self.dest = None
        for vertex, weight in self.weights.items():
            if weight == 0:
                if self.source:
                    self.dest = vertex
                else:
                    self.source = vertex

    def _get_adjacent(vertex: Tuple[int, int]):
        pass

    def calculate_shortest_path(self):
        pass