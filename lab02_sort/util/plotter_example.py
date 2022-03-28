from plotter import BenchmarkPlotter


example_benchmark_data = {"Insertion sort": {1000: 0.0234234, 2000: 0.0523423,
                                             3000: 0.0721523, 4000: 0.0924145},
                          "Quicksort": {1000: 0.01231, 2000: 0.02123,
                                        3000: 0.03521, 4000: 0.04523},
                          "Merge sort": {1000: 0.00231, 2000: 0.00223,
                                         3000: 0.0035241, 4000: 0.0048263},
                          "Bubble sort": {1000: 0.01214, 2000: 0.025432,
                                          3000: 0.055432, 4000: 0.0924145}}


def save_example_to_png():
    bp = BenchmarkPlotter("", "mean")
    bp._make_plot(example_benchmark_data)
    bp._save_results_to_file("example.png")


if __name__ == "__main__":
    save_example_to_png()
