def parse_log_line(line):
    parts = line.split(" ", 3)
    level = parts[2].strip("[]")
    node_and_message = parts[3].split(": ", 1)

    return {
        "date": parts[0],
        "time": parts[1],
        "level": level,
        "node": node_and_message[0],
        "message": node_and_message[1]
    }


def print_error_logs(log_lines):
    # Print only the log lines whose level is ERROR, in a readable format
    for line in log_lines:
        parsed = parse_log_line(line)
        if parsed["level"] == "ERROR":
            print(f"🚨 [{parsed['date']} {parsed['time']}] {parsed['node']} → {parsed['message']}")


if __name__ == "__main__":
    log_lines = [
        "2024-06-01 14:32:10 [ERROR] node-3: Connection timeout after 30s",
        "2024-06-01 14:33:01 [INFO] node-1: Health check passed",
        "2024-06-01 14:35:22 [ERROR] node-2: Disk usage above 90%",
    ]

    print_error_logs(log_lines)