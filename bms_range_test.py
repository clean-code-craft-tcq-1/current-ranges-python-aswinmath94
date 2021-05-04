import unittest
import bms_monitoring_ranges


class CurrentRangesTest(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(bms_monitoring_ranges.check_if_valid_input([1,2,3,4,5,6,8,9, 15,18,22]) == True)
        self.assertTrue(bms_monitoring_ranges.check_if_valid_input([]) == False)
        self.assertTrue(bms_monitoring_ranges.get_continous_range_count([1, 2, 3, 4, 5, 6, 8, 9, 15, 18, 22]) == 'Success')
        self.assertTrue(bms_monitoring_ranges.get_continous_range_count([]) == 'Invalid Input')

    def test_pass(self):
        self.assertFalse(bms_monitoring_ranges.get_continous_range_count([1, 2, 3, 4, 5, 6, 8, 9, 15, 18, 22]) == 'Invalid Input')


if __name__ == '__main__':
    unittest.main()
