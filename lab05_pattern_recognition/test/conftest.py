# from lab04_heaps.util.plotter import BenchmarkPlotter
from lab05_pattern_recognition.src import find_n, find_kr

# benchmark
BENCHMARKED_FUNCTIONS = [find_n, find_kr]
TEST_FILE_PATH = './pan-tadeusz-windows.txt'
BENCHMARK_SAMPLE_SIZES = list(range(5, 25, 5))
# BENCHMARK_SAMPLE_SIZES = list(range(100, 1100, 100))   # this is super slow, do not enable for testing purposes

# plotting results
RESULTS_JSON_PATH = './.benchmarks/report.json'  # must match pytest.ini
STAT = 'mean'

# def pytest_unconfigure(config):
#     """Runs after executing all tests, plot benchmark results from a specified file"""
#     bp = BenchmarkPlotter(RESULTS_JSON_PATH, STAT)
#     with open(RESULTS_JSON_PATH, mode='r'):
#         pass  # throw exception if results file was not created
#     bp.plot_results()
