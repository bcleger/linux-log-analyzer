import re
import sys
import json
from collections import Counter

LOG_FILE = sys.argv[1] if len(sys.argv) > 1 else "sample.log"

def parse_log(file_path):
    errors = 0
    ssh_failed = 0
    ip_counter = Counter()

    try:
        with open(file_path, "r") as file:
            for line in file:
                if "error" in line.lower():
                    errors += 1

                if "Failed password" in line:
                    ssh_failed += 1

                    match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
                    if match:
                        ip_counter[match.group()] += 1

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    return errors, ssh_failed, ip_counter


def print_summary(errors, ssh_failed, ip_counter):
    print("==== LOG ANALYSIS SUMMARY ====")
    print(f"Total Errors: {errors}")
    print(f"Failed SSH Attempts: {ssh_failed}")

    print("\nTop IPs:")
    for ip, count in ip_counter.most_common(3):
        print(f"{ip} -> {count} attempts")


if __name__ == "__main__":
    errors, ssh_failed, ip_counter = parse_log(LOG_FILE)
    print_summary(errors, ssh_failed, ip_counter)


def export_to_json(errors, ssh_failed, ip_counter):
    data = {
        "errors": errors,
        "ssh_failed": ssh_failed,
        "top_ips": ip_counter.most_common(3)
    }

    with open("report.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    errors, ssh_failed, ip_counter = parse_log(LOG_FILE)
    print_summary(errors, ssh_failed, ip_counter)
    export_to_json(errors, ssh_failed, ip_counter)