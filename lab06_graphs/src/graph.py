import math
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
                    return
                else:
                    self.source = vertex

    def _relax(self, u, v):
        potential_dist = self.distances[u] + self.weights[v]
        if self.distances[v] > potential_dist:
            self.distances[v] = potential_dist
            self.predecessors[v] = u
            self.vertex_queue.put(PrioritizedItem(potential_dist, v))

    def _get_adjacent(self, vertex: Tuple[int, int]):
        row, column = vertex
        adjacent_list = []
        if row > 0:
            adjacent_list.append((row - 1, column))
        if column > 0:
            adjacent_list.append((row, column - 1))
        if row < self.height - 1:
            adjacent_list.append((row + 1, column))
        if column < self.width - 1:
            adjacent_list.append((row, column + 1))
        return adjacent_list

    def calculate_shortest_path(self):
        self._find_source_dest()
        self.vertex_queue = PriorityQueue()
        self.vertex_queue.put(PrioritizedItem(0, self.source))
        self.predecessors = {}
        self.distances = {vertex: math.inf for vertex in self.weights.keys()}
        self.distances[self.source] = 0
        while not self.vertex_queue.empty():
            u = self.vertex_queue.get().item
            for v in self._get_adjacent(u):
                self._relax(u, v)
        return self._get_shortest_path()

    def _get_shortest_path(self):
        if self.source == self.dest:
            return [self.source]
        path = []
        curr_vertex = self.dest
        while curr_vertex != self.source:
            path.append((curr_vertex, self.weights[curr_vertex]))
            curr_vertex = self.predecessors[curr_vertex]
        path.append((self.source, 0))
        path.reverse()
        return path
