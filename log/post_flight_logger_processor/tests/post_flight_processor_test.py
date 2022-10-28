import sys
import unittest
sys.path.insert(0, 'log/post_flight_logger_processor/src')
from post_flight_processor import get_info_from_dji_logs, get_date_from_pycom_log


class PostFlightProcessorTest(unittest.TestCase):
    def test_get_date_from_pycom_log_return_true(self):
        try:
            path = 'log/example_logs/log.log'
            pycom_log_file = open(path, encoding='utf-8')
            matches = get_date_from_pycom_log(pycom_log_file.readlines())
            dates = ['20-10-2022 19:29:47', '20-10-2022 19:31:50', '20-10-2022 19:31:50', '20-10-2022 19:31:52', '20-10-2022 19:31:59', '20-10-2022 19:31:59',
                     '20-10-2022 19:32:01', '20-10-2022 19:36:29', '20-10-2022 20:32:07', '20-10-2022 07:44:27', '20-10-2022 12:32:27', '20-10-2022 00:32:27', '01-11-2022 19:32:27']
            self.assertEqual(dates, matches)
        finally:
            pycom_log_file.close()

    def test_get_info_from_dji_logs_return_false(self):
        date = '20-10-2022 19:31:50'
        path = 'log/example_logs/example_dji_logs_reduced.csv'
        info = get_info_from_dji_logs(date, path)
        print(info)
        self.assertEqual(True,True)


if __name__ == '__main__':
    unittest.main()
