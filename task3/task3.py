from functions import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_03/main.py <path_to_log_file> [log_level]")
        return

    log_file_path = sys.argv[1]
    try: 
        logs = load_logs(log_file_path)
        log_counts = count_logs_by_level(logs)
        display_log_counts(log_counts)

        if len(sys.argv) > 2: 
            filter_level = sys.argv[2].upper()
            filtered_logs = filter_logs_by_level(logs, filter_level)
            if filtered_logs:
                for log in filtered_logs:
                    print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
            else:
                print(f"No logs found for level: {filter_level}") 
            
    except (FileNotFoundError, Exception) as e:
        print(f"Error: {e}") 

if __name__ == "__main__":
    main()

    