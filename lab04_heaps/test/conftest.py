from lab04_heaps.util.plotter import BenchmarkPlotter


MIN_RANDOM_ARRAY_LENGTH = 1
MAX_RANDOM_ARRAY_LENGTH = 100
MIN_RANDOM_ARRAY_VALUE = 0
MAX_RANDOM_ARRAY_VALUE = 10000

RANDOM_ARRAY_COUNT = 100

MIN_RANDOM_CHILDREN_COUNT = 2
MAX_RANDOM_CHILDREN_COUNT = 10

BENCHMARK_DATASET_SAMPLE_SIZE = 10000
BENCHMARK_DATASET_RANGE_UPPER = 30001

BENCHMARK_ROUNDS = 5

# plotting results
RESULTS_JSON_PATH = './.benchmarks/report.json'  # must match pytest.ini
STAT = 'mean'


def pytest_unconfigure(config):
    """Runs after executing all tests, plot benchmark results from a specified file"""
    bp = BenchmarkPlotter(RESULTS_JSON_PATH, STAT)
    with open(RESULTS_JSON_PATH, mode='r'):
        pass  # throw exception if results file was not created
    bp.plot_results()
