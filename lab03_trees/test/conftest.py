from lab03_trees.src import make_avl, make_bst
from lab03_trees.util.plotter import BenchmarkPlotter

# region test-bst
BST_RANDOM_RANGE_LOWER = 0
BST_RANDOM_RANGE_UPPER = 50000
BST_RANDOM_NUM_SAMPLES = 2000
BST_RANDOM_NUM_DATASETS = 100

BST_INVALID_FIND_TEST_ITERATIONS = 5

# region benchmark
BENCHMARK_SAMPLE_SIZES = list(range(1000, 11000, 1000))
BENCHMARK_MAKE_FUNCTIONS = [make_avl, make_bst]
BENCHMARK_DATASET_SAMPLE_SIZE = 10000
BENCHMARK_DATASET_RANGE_UPPER = 30001


# plotting results
RESULTS_JSON_PATH = './.benchmarks/report.json'  # must match pytest.ini
STAT = 'mean'


def pytest_unconfigure(config):
    """Runs after executing all tests, plot benchmark results from a specified file"""
    bp = BenchmarkPlotter(RESULTS_JSON_PATH, STAT)
    with open(RESULTS_JSON_PATH, mode='r'):
        pass  # throw exception if results file was not created
    bp.plot_results()
