import sys
import unittest
sys.path.insert(0, 'LOG/post_flight_logger_processor/src')
from csv_handler import replace_slash_by_middle_dash, format_time, format_date, to_24_format


class CsvHandlerTest(unittest.TestCase):
    def test_replace_slash_by_middle_dash_return_true(self):
        date = '5/9/2020'
        self.assertEqual(replace_slash_by_middle_dash(date), '05-09-2020')

    def test_format_hour_return_true(self):
        hour = '8:42:30.38 PM'
        self.assertEqual(format_time(hour), '08:42:30')

    def test_format_date_return_true(self):
        dates = ['5/9/2020', '10/10/2020', '5/12/2020']
        hours = ['8:42:30.38 PM', '10:42:30.38 PM', '11:00:15.38 AM']
        new_dates = ['05-09-2020 08:42:30',
                     '10-10-2020 10:42:30', '05-12-2020 11:00:15']

        self.assertEqual(format_date(dates, hours), new_dates)

    def test_to_24_format_return_true(self):
        time = '8:36:29.02 PM'
        self.assertEqual(to_24_format(time), 20)


if __name__ == '__main__':
    unittest.main()
