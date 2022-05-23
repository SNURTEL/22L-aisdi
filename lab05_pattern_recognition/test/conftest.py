# from lab04_heaps.util.plotter import BenchmarkPlotter
from lab05_pattern_recognition.src import find_n, find_kr, find_kmp
from lab05_pattern_recognition.util.plotter import BenchmarkPlotter

# benchmark
BENCHMARKED_FUNCTIONS = [find_n, find_kr, find_kmp]
TEST_FILE_PATH = '/home/jani/repos/python/22l-aisdi-kowalczewski-owienko/lab05_pattern_recognition/test/pan-tadeusz-unix.txt'
# BENCHMARK_SAMPLE_SIZES = list(range(5, 25, 5))
BENCHMARK_SAMPLE_SIZES = list(range(100, 1100, 100))   # this is super slow, do not enable for testing purposes

# plotting results
RESULTS_JSON_PATH = '/home/jani/repos/python/22l-aisdi-kowalczewski-owienko/lab05_pattern_recognition/test/.benchmarks/report.json'  # must match pytest.ini
STAT = 'mean'

# comparison tests
COMPARISON_DATASET_ALPHABET = "ab"
COMPARISON_TEXT_SIZES = list(range(0, 100, 2))
COMPARISON_PATTERN_SIZES = list(range(0, 100, 2))
DATASETS_PER_SIZE = 5


def pytest_unconfigure(config):
    """Runs after executing all tests, plot benchmark results from a specified file"""
    bp = BenchmarkPlotter(RESULTS_JSON_PATH, STAT)
    with open(RESULTS_JSON_PATH, mode='r'):
        pass  # throw exception if results file was not created
    bp.plot_results()
