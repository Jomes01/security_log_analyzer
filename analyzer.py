import re
import pandas as pd
from datetime import datetime
from collections import defaultdict

class SecurityLogAnalyzer:
    def __init__(self, filename):
        self.log_file = filename
        self.logs = self.parse_logs()

    def parse_logs(self):
        # Define regex patterns for various log events
        log_patterns = {
            'auth': r'(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}).*?(\d{1,3}(?:\.\d{1,3}){3}).*?Failed password for (\w+)',
            'web': r'(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}).*?(\d{1,3}(?:\.\d{1,3}){3}).*?".*?" \d+ \d+',
            'invalid_user': r'(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}).*?(\d{1,3}(?:\.\d{1,3}){3}).*?Invalid user (\w+)',
        }

        logs = defaultdict(list)

        with open(self.log_file, 'r') as file:
            for line in file:
                log_matched = False
                for log_type, pattern in log_patterns.items():
                    match = re.search(pattern, line)
                    if match:
                        log_matched = True
                        timestamp_str = match.group(1)
                        try:
                            timestamp = datetime.strptime(timestamp_str, "%b %d %H:%M:%S")
                        except ValueError:
                            print(f"Invalid timestamp: {timestamp_str}")
                            continue

                        logs['timestamp'].append(timestamp)
                        logs['ip_address'].append(match.group(2))
                        logs['event_type'].append(log_type)

                        if log_type in ['auth', 'invalid_user']:
                            logs['username'].append(match.group(3))
                        else:
                            logs['username'].append(None)
                        break

                if not log_matched:
                    print(f"Warning: Unmatched log entry: {line.strip()}")

        return pd.DataFrame(logs)

    def generate_report(self):
        output_file = 'security_report.csv'
        self.logs.to_csv(output_file, index=False)
        print(f"\n✅ Report generated: {output_file}")

# Example usage
if __name__ == "__main__":
    file_name = input("Enter the log file name (e.g., auth.log): ")
    analyzer = SecurityLogAnalyzer(file_name)
    analyzer.generate_report()
