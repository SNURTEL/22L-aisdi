from lab03_trees.test.conftest import RESULTS_JSON_PATH, STAT
from lab03_trees.util.plotter import BenchmarkPlotter

if __name__ == '__main__':
    bp = BenchmarkPlotter(RESULTS_JSON_PATH, STAT)
    with open(RESULTS_JSON_PATH, mode='r'):
        pass  # throw exception if results file was not created
    bp.plot_results()
