import pytest
from ..src import insertion_sort, quicksort
from ..util import BenchmarkPlotter

# benchmark
BENCHMARKED_FUNCTIONS = [insertion_sort, quicksort]
TEST_FILE_PATH = '../pan-tadeusz-unix.txt'
BENCHMARK_SAMPLE_SIZES = list(range(1000, 11000, 1000))

# control runs
CONTROL_REPS = 100
SAMPLE_RANGE_LOWER = 0
SAMPLE_RANGE_UPPER = 10000
NUM_SAMPLES = 1000

# plotting results
RESULTS_JSON_PATH = './.benchmarks/report.json'  # must match pytest.ini


@pytest.fixture(scope='module')
def plot_results():
    """Plot benchmark results from a specified file"""
    bp = BenchmarkPlotter(RESULTS_JSON_PATH)
    with open(RESULTS_JSON_PATH, mode='r'):
        pass  # throw exception if file was not created
    bp.plot_results()
