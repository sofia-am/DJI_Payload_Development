import re
from csv_handler import get_drone_sensors_data

MERGED_LOG_PATH = 'log/post_flight_logger_processor/merged_log.log'


def merge_logs_files():
    try:
        path = input('Write pycom log file path\n')
        csv_path = input("Write the path to the .csv file\n")
        pycom_log_file = open(path, encoding='utf-8')
        lines = pycom_log_file.readlines()
        dates = get_date_from_pycom_log(lines)
        write_merged_file(dates, lines, csv_path)
    finally:
        pycom_log_file.close()


def get_date_from_pycom_log(log_list):
    matches = []
    for line in log_list:
        matches.append(re.findall(r'\[(\d+.*?)\]', line)[0])

    return matches


def get_info_from_dji_logs(date, csv_path):
    df = get_drone_sensors_data(csv_path)
    info = df.loc[df['Date'] == date]
    return info.iloc[0]


def write_merged_file(dates, lines, csv_path):
    try:
        log_file = open(MERGED_LOG_PATH, "a+")
        for i in range(0, len(dates)):
            info = get_info_from_dji_logs(dates[i], csv_path)
            log_file.write(f'{lines[i]}')
            if i == len(dates) - 1:
                log_file.write('\n')
            log_file.write(
                f'Lat = {info.loc["Lat"]} || Lon = {info.loc["Lon"]} || Height[ft] = {info.loc["Hei[ft]"]} || Altitud[ft] = {info.loc["Alt[ft]"]}\n')
    finally:
        log_file.close()


merge_logs_files()
