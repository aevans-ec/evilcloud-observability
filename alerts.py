from typing import Callable, Dict

class EvilCloudAlerts:
    def __init__(self):
        self.rules = {}

    def add_rule(self, metric: str, threshold: float, callback: Callable):
        self.rules[metric] = {"threshold": threshold, "callback": callback}

    def check(self, metrics: Dict[str, float]):
        for metric, data in self.rules.items():
            if metric in metrics and metrics[metric] > data["threshold"]:
                data["callback"](metric, metrics[metric])
