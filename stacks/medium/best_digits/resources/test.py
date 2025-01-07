import json

import unittest
from stacks.medium.best_digits.program import bestDigits


class Test(unittest.TestCase):
        def test1(self):
            with open("testcase1.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test2(self):
            with open("testcase2.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test3(self):
            with open("testcase3.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test4(self):
            with open("testcase4.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test5(self):
            with open("testcase5.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test6(self):
            with open("testcase6.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test7(self):
            with open("testcase7.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test8(self):
            with open("testcase8.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test9(self):
            with open("testcase9.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test10(self):
            with open("testcase10.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test11(self):
            with open("testcase11.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test12(self):
            with open("testcase12.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test13(self):
            with open("testcase13.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test14(self):
            with open("testcase14.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test15(self):
            with open("testcase15.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test16(self):
            with open("testcase16.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test17(self):
            with open("testcase17.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)

        def test18(self):
            with open("testcase18.json") as file:
                test_data = json.load(file)

            number = test_data["input"]["number"]
            numDigits = test_data["input"]["numDigits"]
            expected_output = test_data["expected"]
            actual_output = bestDigits(number, numDigits)

            self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()