# test_program.py
import unittest
import json
from strings.medium.one_edit.program import oneEdit


def load_test_case(filename):
    with open(filename) as file:
        return json.load(file)


class Test(unittest.TestCase):

    def test1(self):
        test_data = load_test_case("testcase1.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test2(self):
        test_data = load_test_case("testcase2.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test3(self):
        test_data = load_test_case("testcase3.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test4(self):
        test_data = load_test_case("testcase4.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test5(self):
        test_data = load_test_case("testcase5.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test6(self):
        test_data = load_test_case("testcase6.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test7(self):
        test_data = load_test_case("testcase7.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test8(self):
        test_data = load_test_case("testcase8.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test9(self):
        test_data = load_test_case("testcase9.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test10(self):
        test_data = load_test_case("testcase10.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test11(self):
        test_data = load_test_case("testcase11.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test12(self):
        test_data = load_test_case("testcase12.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test13(self):
        test_data = load_test_case("testcase13.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test14(self):
        test_data = load_test_case("testcase14.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test15(self):
        test_data = load_test_case("testcase15.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test16(self):
        test_data = load_test_case("testcase16.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test17(self):
        test_data = load_test_case("testcase17.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test18(self):
        test_data = load_test_case("testcase18.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test19(self):
        test_data = load_test_case("testcase19.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test20(self):
        test_data = load_test_case("testcase20.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test21(self):
        test_data = load_test_case("testcase21.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test22(self):
        test_data = load_test_case("testcase22.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test23(self):
        test_data = load_test_case("testcase23.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test24(self):
        test_data = load_test_case("testcase24.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test25(self):
        test_data = load_test_case("testcase25.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test26(self):
        test_data = load_test_case("testcase26.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test27(self):
        test_data = load_test_case("testcase27.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test28(self):
        test_data = load_test_case("testcase28.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test29(self):
        test_data = load_test_case("testcase29.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test30(self):
        test_data = load_test_case("testcase30.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test31(self):
        test_data = load_test_case("testcase31.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)

    def test32(self):
        test_data = load_test_case("testcase32.json")
        stringOne = test_data["input"]["stringOne"]
        stringTwo = test_data["input"]["stringTwo"]
        expected = test_data["expected"]
        self.assertEqual(oneEdit(stringOne, stringTwo), expected)



if __name__ == '__main__':
    unittest.main()