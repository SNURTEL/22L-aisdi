import argparse
from distutils.util import convert_path
from graph import Graph
from file_console_io import convert_vertex_path_to_str, load_weights, print_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("filepath", help="Source file path")
    args = ap.parse_args()
    filepath = args.filepath
    with open(filepath, mode="r") as fp:
        weights, width, height = load_weights(fp)
    graph = Graph(weights, width, height)
    path = graph.calculate_shortest_path()
    path_str = convert_vertex_path_to_str(path)
    print(path_str)


if __name__ == "__main__":
    main()
