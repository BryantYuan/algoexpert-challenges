import unittest
import json
from stacks.hard.largest_rectangle_under_skyline.program import largestRectangleUnderSkyline


def load_test_case(filename):
    """Helper function to load a test case from a JSON file."""
    with open(filename) as file:
        return json.load(file)


class TestLargestRectangle(unittest.TestCase):

    def test_case_1(self):
        test_data = load_test_case("testcase1.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_2(self):
        test_data = load_test_case("testcase2.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_3(self):
        test_data = load_test_case("testcase3.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_4(self):
        test_data = load_test_case("testcase4.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_5(self):
        test_data = load_test_case("testcase5.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_6(self):
        test_data = load_test_case("testcase6.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_7(self):
        test_data = load_test_case("testcase7.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_8(self):
        test_data = load_test_case("testcase8.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_9(self):
        test_data = load_test_case("testcase9.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_10(self):
        test_data = load_test_case("testcase10.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_11(self):
        test_data = load_test_case("testcase11.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_12(self):
        test_data = load_test_case("testcase12.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_13(self):
        test_data = load_test_case("testcase13.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_14(self):
        test_data = load_test_case("testcase14.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_15(self):
        test_data = load_test_case("testcase15.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)

    def test_case_16(self):
        test_data = load_test_case("testcase16.json")
        input_data = test_data["input"]["buildings"]
        expected = test_data["expected"]
        self.assertEqual(largestRectangleUnderSkyline(input_data), expected)


if __name__ == "__main__":
    unittest.main()