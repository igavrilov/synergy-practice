import unittest

from sum_negatives import find_sum_between_min_and_max_element


class TestFindSumBetweenMinAndMaxElement(unittest.TestCase):

    def test_empty_list_raises_exception(self):
        with self.assertRaises(AssertionError):
            find_sum_between_min_and_max_element([])

    def test_argument_must_be_gt_1(self):
        with self.assertRaises(AssertionError):
            find_sum_between_min_and_max_element([1])
        find_sum_between_min_and_max_element([0, 0])

    def test_no_negative_elements_returns_0(self):
        self.assertEqual(
            find_sum_between_min_and_max_element([1, 2]),
            0
        )

    def test_one_negative_element_in_list_of_two_elements_returns_0(self):
        self.assertEqual(
            find_sum_between_min_and_max_element([10, -10]),
            0
        )

    def test_one_negative_element_returns_this_element(self):
        self.assertEqual(
            find_sum_between_min_and_max_element([1000, -5, -100]),
            -5
        )

    def test_two_intervals_sum_in_the_beginning(self):
        self.assertEqual(
            #                                     max                min
            find_sum_between_min_and_max_element([100, -1, -1, -1, -1000, -99, -2, -2, -2, 50, 5, 7, 29, 99]),
            -3
        )

    def test_two_intervals_sum_in_the_end(self):
        self.assertEqual(
            #                                                           max              min
            find_sum_between_min_and_max_element([50, -1, -1, -1, -999, 51, -2, -2, -2, -1000, 5, 6, 7, 8, 9]),
            -6
        )


if __name__ == '__main__':
    unittest.main()
