from src.file_console_io import TooLittleChars, convert_vertex_path_to_str, load_weights
from io import StringIO
import pytest


def test_load_weights_empty():
    fp = StringIO("")
    weights, width, height = load_weights(fp)
    assert weights == {}
    assert width == 0
    assert height == 0


def test_load_weights_single():
    fp = StringIO("1\n")
    weights, width, height = load_weights(fp)
    assert weights == {(0, 0): 1}
    assert width == 1
    assert height == 1


def test_load_weights_multiple():
    fp = StringIO("26\n")
    weights, width, height = load_weights(fp)
    assert weights == {(0, 0): 2, (0, 1): 6}
    assert width == 2
    assert height == 1


def test_load_weights_multiple_rows():
    fp = StringIO("26\n19\n")
    weights, width, height = load_weights(fp)
    assert weights == {(0, 0): 2, (0, 1): 6, (1, 0): 1, (1, 1): 9}
    assert width == 2
    assert height == 2


def test_load_weights_too_much_chars():
    fp = StringIO("26\n192\n")
    weights, width, height = load_weights(fp)
    assert weights == {(0, 0): 2, (0, 1): 6, (1, 0): 1, (1, 1): 9}
    assert width == 2
    assert height == 2


def test_load_weights_too_little_chars():
    fp = StringIO("26\n1\n")
    with pytest.raises(TooLittleChars):
        load_weights(fp)


def test_convert_path_1():
    assert convert_vertex_path_to_str([((0, 0), 0), ((0, 1), 1), ((0, 2), 0)], 3, 1) == "010\n"


def test_convert_path_2():
    assert convert_vertex_path_to_str([((0, 0), 0), ((0, 1), 9), ((1, 1), 0)], 2, 2) == "09\n 0\n"