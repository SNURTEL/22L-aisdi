import enum
from io import TextIOWrapper
from typing import Dict, Tuple
from unittest import result

class TooLittleChars(Exception):
    def __init__(self):
        super().__init__("Too little chars in provided file")


def load_weights(fp: TextIOWrapper) -> Tuple[Dict[Tuple[int, int], int], int, int]:
    line = True
    row = 0
    width = 0
    weights = {}
    line = fp.readline()[:-1]
    for char_num, char in enumerate(line):
        width += 1
        weights[(row, char_num)] = int(char)
    if line:
        row += 1
    line = fp.readline()[:-1]
    while(line):
        if width > 0 and len(line) < width:
            raise TooLittleChars
        for char_num in range(width):
            weights[(row, char_num)] = int(line[char_num])
        row += 1
        line = fp.readline()[:-1]
    return weights, width, row


def convert_vertex_path_to_str(vertex_path, width, height) -> str:
    source = vertex_path[0]
    dest = vertex_path[-1]
    vertex_path = vertex_path[1:-1]
    result_str = ""
    for row in range(height):
        for column in range(width):
            if (row, column) == source or (row, column) == dest:
                result_str += "0"
            elif (row, column) in vertex_path:
                result_str += "1"
            else:
                result_str += " "
        result_str += "\n"
    return result_str
