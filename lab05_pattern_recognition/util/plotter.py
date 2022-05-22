from matplotlib import pyplot as plt
import json

from types import SimpleNamespace
from operator import attrgetter


class BenchmarkPlotter:
    def __init__(self, results_json_path: str, stat: str):
        self._results_filepath = results_json_path
        self.stat = stat

    def plot_results(self) -> None:
        """Plots benchmark results"""
        all_benchmark_data = self._get_benchmark_data_from_json(self.stat)
        for benchmark_name, benchmark_data in all_benchmark_data.items():
            self._make_plot(benchmark_data, benchmark_name)
            filename = f"./plots/{benchmark_name.lower().replace(' ', '_')}.png"
            print(f"Plot '{benchmark_name}': Success! Saving results to {filename}")
            self._save_results_to_file(filename)

    def _make_plot(self, benchmark_data: dict, function_name: str) -> None:  # Dict[str, Dict[int, float]]
        """Builds and configures the plot"""
        plt.clf()
        plt.cla()
        for func, results in benchmark_data.items():
            keys = results.keys()
            values = results.values()
            plt.plot(keys, values, label=func)
        plt.legend()
        plt.title(label=f"{function_name}: {self.stat} stat")
        plt.xlabel("Number of words")
        plt.ylabel("Time [ms]")

    def _save_results_to_file(self, filename: str) -> None:
        """Saves the plot to a .png file"""
        plt.savefig(filename)

    def _get_benchmark_data_from_json(self, stat: str = "mean") -> dict:  # Dict[str: Dict[str, Dict[int, float]]]:
        """Extracts benchmark results from a .json file"""
        with open(self._results_filepath, mode='r', encoding='utf-8') as fp:
            raw_data = BenchmarkPlotter._deserialize_json(fp)
        a = attrgetter(stat)

        grouped_records = {}
        for record in raw_data.benchmarks:
            try:
                grouped_records[record.extra_info.friendly_name].append(record)
            except KeyError:
                grouped_records[record.extra_info.friendly_name] = [record]

        all_results = {}

        for benchmark_name, single_benchmark_dataset in grouped_records.items():
            extracted = {tuple(record.param.split('-')): a(record.stats)
                         for record in single_benchmark_dataset}
            function_names = {k[0] for k, v in extracted.items()}
            results = {func.replace("make_", " ").capitalize(): {int(k[1]): v
                                                                 for k, v in extracted.items() if k[0] == func}
                       for func in function_names}

            all_results[benchmark_name] = results

        return all_results

    @staticmethod
    def _deserialize_json(fp) -> SimpleNamespace:
        """Reads JSON data from fp and deserializes it into a SimpleNamespace object"""
        data_obj = json.load(fp, object_hook=lambda d: SimpleNamespace(**d))
        return data_obj
