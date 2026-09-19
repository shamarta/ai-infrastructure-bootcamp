def parse_log_line(line) :
    parts = line.split(" " , 3)
    level = parts[2].strip("[]")    
    node_and_message = parts[3].split(": ", 1)

    result = {
            "date" : parts[0],
            "time" : parts[1],
            "level" : level,
            "node" : node_and_message[0],
            "message" : node_and_message[1]
    }
    return result
line = "2024-06-01 14:32:10 [ERROR] node-3: Connection timeout after 30s"
print(parse_log_line(line))