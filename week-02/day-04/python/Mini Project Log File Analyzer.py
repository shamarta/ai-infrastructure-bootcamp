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


def write_sample_log(filename):
    lines = [
        "2024-06-01 14:32:10 [ERROR] node-3: Connection timeout after 30s",
        "2024-06-01 14:33:01 [INFO] node-1: Health check passed",
        "2024-06-01 14:35:22 [ERROR] node-2: Disk usage above 90%",
        "2024-06-01 14:36:05 [WARNING] node-4: High memory usage",
    ]
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")


def analyze_log_file(filename):
    try:
        with open(filename, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Log file '{filename}' not found.")
        return

    error_count = 0
    for line in lines:
        parsed = parse_log_line(line)
        if parsed["level"] == "ERROR":
            error_count += 1
            print(f"🚨 [{parsed['date']} {parsed['time']}] {parsed['node']} → {parsed['message']}")

    print(f"\nTotal lines: {len(lines)}")
    print(f"Error lines: {error_count}")


if __name__ == "__main__":
    write_sample_log("server.log")
    analyze_log_file("server.log")