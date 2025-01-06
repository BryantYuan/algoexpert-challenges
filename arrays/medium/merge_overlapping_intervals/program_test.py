import json
import unittest
import program


class Test(unittest.TestCase):
    def test1(self):
        with open("resources/testcase1.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)

    def test2(self):
        with open("resources/testcase2.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)

    def test3(self):
        with open("resources/testcase3.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)

    def test4(self):
        with open("resources/testcase4.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)

    def test5(self):
        with open("resources/testcase5.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)

    def test6(self):
        with open("resources/testcase6.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)

    def test7(self):
        with open("resources/testcase7.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)

    def test8(self):
        with open("resources/testcase8.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)

    def test9(self):
        with open("resources/testcase9.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)

    def test10(self):
        with open("resources/testcase10.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)

    def test11(self):
        with open("resources/testcase11.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)

    def test12(self):
        with open("resources/testcase12.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)

    def test13(self):
        with open("resources/testcase13.json") as test_info:
            test_case = json.load(test_info)

        intervals = test_case["input"]
        expected = test_case["expected"]
        actual = program.mergeOverlappingIntervals(intervals)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()