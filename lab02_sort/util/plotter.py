from matplotlib import pyplot as plt
import json

from types import SimpleNamespace
from operator import attrgetter


STAT = "mean"

class BenchmarkPlotter:
    def __init__(self, results_json_path: str):
        self._results_filepath = results_json_path
        self.stat = "mean"

    def plot_results(self) -> None:
        """Plots benchmark results"""
        print("success!")
        benchmark_data = self._get_benchmark_data_from_json(STAT)
        self._make_plot(benchmark_data)
        self._save_results_to_file("plot.png")

    def _make_plot(self, benchmark_data: dict[str, dict]) -> None:
        """Builds and configures the plot"""
        for func, results in benchmark_data.items():
            keys = results.keys()
            values = results.values()
            plt.plot(keys, values, label=func)
        plt.legend()
        plt.title(label=f"Function benchmark: {STAT} stat")

    def _save_results_to_file(self, filename: str) -> None:
        """Saves the plot to a .png file"""
        plt.savefig(filename)

    def _get_benchmark_data_from_json(self, stat: str = "mean") -> dict:
        """Extracts benchmark results from a .json file"""
        # Example returned data structure (Dict[str: Dict[int, float]], typehints refused to work):
        # {"Insertion sort" : {
        #       1000: 0.0234234,
        #       2000: 0.0523423,
        #       ...
        #       },
        # "Quicksort": {
        #       1000: 0.01231,
        #       2000: 0.02123,
        #       ...
        #       }
        #   }

        with open(self._results_filepath, mode='r', encoding='utf-8') as fp:
            raw_data = BenchmarkPlotter._deserialize_json(fp)
        a = attrgetter(stat)
        extracted = {tuple(record.param.split('-')): a(record.stats) for record in raw_data.benchmarks}
        function_names = {k[0] for k, v in extracted.items()}
        results = {func.replace("_", " ").capitalize(): {int(k[1]): v for k, v in extracted.items() if k[0] == func} for
                   func
                   in function_names}
        return results

    @staticmethod
    def _deserialize_json(fp) -> SimpleNamespace:
        """Reads JSON data from fp and deserializes it into a SimpleNamespace object"""
        data_obj = json.load(fp, object_hook=lambda d: SimpleNamespace(**d))
        return data_obj
