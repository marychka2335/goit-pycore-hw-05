from collections import Counter

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }
    
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
                 for line in file:
                     logs.append(parse_log_line(line))
    except FileNotFoundError:
             raise FileNotFoundError(f"File not found: {file_path}") # Поднимаем исключение
    except Exception as e:
             raise Exception(f"Error loading logs from {file_path}: {e}") # Поднимаем исключение
         
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    return dict(Counter(log['level'] for log in logs))


def display_log_counts(counts: dict):
    print("Log Level | Count")
    print("----------|------")
    for level, count in counts.items():
        print(f"{level.upper():<9} | {count}")