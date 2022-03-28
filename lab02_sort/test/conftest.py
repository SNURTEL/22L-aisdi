from ..src import insertion_sort, quicksort, merge_sort, bubble_sort
from ..util import BenchmarkPlotter

# benchmark
BENCHMARKED_FUNCTIONS = [insertion_sort, quicksort, merge_sort, bubble_sort]
TEST_FILE_PATH = '../pan-tadeusz-unix.txt'
BENCHMARK_SAMPLE_SIZES = list(range(1000, 11000, 1000))

# control runs
CONTROL_REPS = 100
SAMPLE_RANGE_LOWER = 0
SAMPLE_RANGE_UPPER = 10000
NUM_SAMPLES = 1000

# plotting results
RESULTS_JSON_PATH = './.benchmarks/report.json'  # must match pytest.ini
STAT = 'mean'


def pytest_unconfigure(config):
    """Runs after executing all tests, plot benchmark results from a specified file"""
    bp = BenchmarkPlotter(RESULTS_JSON_PATH, STAT)
    with open(RESULTS_JSON_PATH, mode='r'):
        pass  # throw exception if results file was not created
    bp.plot_results()
