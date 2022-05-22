from lab05_pattern_recognition.util.plotter import BenchmarkPlotter
from lab05_pattern_recognition.test.conftest import RESULTS_JSON_PATH, STAT

if __name__ == '__main__':
    bp = BenchmarkPlotter(RESULTS_JSON_PATH, STAT)
    with open(RESULTS_JSON_PATH, mode='r'):
        pass  # throw exception if results file was not created
    bp.plot_results()
