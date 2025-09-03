import random
import time

class EvilCloudMetrics:
    def __init__(self, service_name: str):
        self.service_name = service_name
        self.metrics = {}

    def record(self, metric: str, value: float):
        if metric not in self.metrics:
            self.metrics[metric] = []
        self.metrics[metric].append(value)

    def get_latest(self, metric: str) -> float:
        return self.metrics.get(metric, [0])[-1]

    def simulate_usage(self):
        self.record("cpu", random.uniform(5, 85))
        self.record("memory", random.uniform(100, 1500))
        self.record("latency_ms", random.uniform(20, 250))
