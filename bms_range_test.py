import unittest
import bms_monitoring_ranges




class test_battery_current_ranges(unittest.TestCase):
    def test_passing_input_validation(self):
        self.assertTrue(bms_monitoring_ranges.current_ranges([]) == "Invalid Input list")


    def test_passing(self):
        self.assertTrue(bms_monitoring_ranges.current_ranges([1,2, 3, 4,6, 7, 10, 11, 12, 13,15,19,25]) == "Valid Input list")

    def test_failing(self):
        self.assertFalse(bms_monitoring_ranges.current_ranges([2,3, 5, 6, 8,9]) == "Invalid Input list")  # no continuous range,should give invalid


if __name__ == '__main__':
    unittest.main()
