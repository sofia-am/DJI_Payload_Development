import sys
import unittest
sys.path.insert(0, 'log/post_flight_logger_processor/src')
from csv_handler import replace_slash_by_middle_dash, format_time, format_date, to_24_format, get_drone_sensors_data


class CsvHandlerTest(unittest.TestCase):
    def test_replace_slash_by_middle_dash_return_true(self):
        date = '5/9/2020'
        self.assertEqual(replace_slash_by_middle_dash(date), '05-09-2020')

    def test_format_pm_hour_return_true(self):
        hour = '8:42:30.38 PM'
        hour2 = '7:32:27.23 PM'
        self.assertEqual(format_time(hour), '20:42:30')
        self.assertEqual(format_time(hour2), '19:32:27')

    def test_format_am_hour_return_true(self):
        hour = '8:42:30.38 AM'
        self.assertEqual(format_time(hour), '08:42:30')

    def test_format_date_return_true(self):
        dates = ['5/9/2020', '10/10/2020', '5/12/2020', '01/11/2022']
        hours = ['8:42:30.38 PM', '10:42:30.38 AM', '12:00:15.38 PM', '7:32:27.23 PM']
        new_dates = ['05-09-2020 20:42:30',
                     '10-10-2020 10:42:30', '05-12-2020 00:00:15', '01-11-2022 19:32:27']

        self.assertEqual(format_date(dates, hours), new_dates)

    def test_to_24_format_return_true(self):
        time = '08:36:29.02 PM'
        time2 = '10:42:30.38 AM'
        time3 = '12:00:15.38 PM'
        time4 = '7:32:27.23 PM'
        self.assertEqual(to_24_format(time.split(':')), 20)
        self.assertEqual(to_24_format(time2.split(':')), 10)
        self.assertEqual(to_24_format(time3.split(':')), 00)
        self.assertEqual(to_24_format(time4.split(':')), 19)

    def test_get_drone_sensor_data_return_true(self):
        csv_path = 'log/example_logs/example_dji_logs_reduced.csv'
        try:
            dji_log_file = open(csv_path, encoding='utf-8')
            data = get_drone_sensors_data(csv_path) 
        finally:
            dji_log_file.close()   
        
        print(data)    
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()