from ..src import insertion_sort, quicksort

# benchmark
BENCHMARKED_FUNCTIONS = [insertion_sort, quicksort]
TEST_FILE_PATH = '../pan-tadeusz-unix.txt'
BENCHMARK_SAMPLE_SIZES = list(range(1000, 11000, 1000))

# control runs
CONTROL_REPS = 100
SAMPLE_RANGE_LOWER = 0
SAMPLE_RANGE_UPPER = 10000
NUM_SAMPLES = 1000
