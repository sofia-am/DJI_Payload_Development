import re
from csv_handler import get_drone_sensors_data


def merge_logs_files():
    try:
        path = input('Write pycom log file path')
        pycom_log_file = open(path, encoding='utf-8')
        date = get_date_from_pycom_log(pycom_log_file)

    finally:
        pycom_log_file.close()


def get_date_from_pycom_log(log_list):
    matches = []
    for line in log_list:
        matches.append(re.findall(r'\[(\d+.*?)\]', line)[0])
        
    return matches
