import datetime
import json
import os

class EvilCloudLogger:
    def __init__(self, service_name: str):
        self.service_name = service_name
        self.logs = []

    def log(self, level: str, message: str):
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "service": self.service_name,
            "level": level.upper(),
            "message": message
        }
        self.logs.append(entry)
        print(f"[{entry['timestamp']}] {entry['level']} - {entry['message']}")

    def export(self, filename: str):
        with open(filename, "w") as f:
            for log in self.logs:
                f.write(json.dumps(log) + "\n")
