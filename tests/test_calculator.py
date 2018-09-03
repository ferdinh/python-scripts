import sys
import os
# get the directory path of this file.
dirname = os.path.dirname(os.path.abspath(__file__))
# get the root of this child directory.
rootdir = os.path.dirname(dirname)
sys.path.append(rootdir)

import mathematics


class TestCalculatorClass(object):

    firstNumber = 10
    secondNumber = 5.5

    def test_add(self):

        # arrange
        expectedResult = 15.5

        # act
        actualResult = mathematics.add(self.firstNumber, self.secondNumber)

        # assert
        assert expectedResult == actualResult

    def test_min(self):

        # arrange
        expectedResult = 4.5

        # act
        actualResult = mathematics.min(self.firstNumber, self.secondNumber)

        # assert
        assert expectedResult == actualResult

    def test_div(self):

        # arrange
        expectedResult = 1.818181818

        # act
        # checks up to 9 decimal place accuracy
        actualResult = round(mathematics.divide(
            self.firstNumber, self.secondNumber), 9)

        # assert
        assert expectedResult == actualResult

    def test_multiply(self):
        # arrange
        expectedResult = 55

        # act
        actualResult = mathematics.multiply(
            self.firstNumber, self.secondNumber)

        # assert
        assert expectedResult == actualResult

    def test_parse_to_rpn(self):
        
        # Arrange
        expected_results = [
            [6.0, 8.0, "/", 9.0, "+", 8.0, 10.0, "*", "-"],
            [3.0, 2.0, "*", 5.0, "+"],
            [5.0, 10.0, "+", 9.0, "*", 8.0, "/"],
            [0.5, 2.0, 4.0, "*", 1.0, "-", "*"],
            [5.0, 4.0, "+", 8.0, "*", 8.0, 10.0, "+", "*"]
        ]

        infix_notations = [
            "6 / 8 + 9 - 8 * 10",
            "3 * 2 + 5",
            "( 5 + 10 ) * 9 / 8",
            "0.5 * ( 2 * 4 - 1 )",
            "( ( 5 + 4 ) * 8 ) * ( 8 + 10 )"
        ]

        actual_results = list()

        # Act
        for notation in infix_notations:
            actual_results.append(mathematics.parse_to_rpn(notation))


        # assert
        index = 0
        for result in expected_results:
            assert actual_results[index] == result
            index += 1

    def test_evaluate_rpn(self):

        # Arrange  
        expected_results = [
            -70.25,
            11.0,
            3.5,
            1296.0
        ]
        
        rpns = [
            [6.0, 8.0, "/", 9.0, "+", 8.0, 10.0, "*", "-"],
            [3.0, 2.0, "*", 5.0, "+"],
            [0.5, 2.0, 4.0, "*", 1.0, "-", "*"],
            [5.0, 4.0, "+", 8.0, "*", 8.0, 10.0, "+", "*"]
        ]

        actual_results = list()

        # Act
        for rpn in rpns:
            actual_results.append(mathematics.evaluate_rpn(rpn))

        # Assert
        index = 0
        for expected in expected_results:
            assert actual_results[index] == expected
            index += 1

    def test_is_number(self):
        # Arrange
        expected_case_1 = True
        number_case_1 = 0.0

        expected_case_2 = False
        str_case_2 = "Hello"

        # Act
        result_case_1 = mathematics.is_number(number_case_1)
        result_case_2 = mathematics.is_number(str_case_2)

        # Assert
        assert result_case_1 == expected_case_1
        assert result_case_2 == expected_case_2

    def test_is_operator(self):
        # Arrange
        expected_test_case_true = True
        expected_test_case_false = False

        test_case_true = ["+", "-", "*", "/"]
        test_case_false = [ "**", "_", 9.0, "!"]

        test_case_true_result = list()
        test_case_false_result = list()

        # Act
        for op in test_case_true:
            test_case_true_result.append(mathematics.is_operator(op))
        
        for op in test_case_false:
            test_case_false_result.append(mathematics.is_operator(op))

        # Assert
        for r in test_case_true_result:
            assert r == expected_test_case_true

        for r in test_case_false_result:
            assert r == expected_test_case_false

    def test_greater_precedence(self):
        # Arrange
        expected_test_case_1 = False
        expected_test_case_2 = True

        test_case_1_operator_1 = "+"
        test_case_1_operator_2 = "-"

        test_case_2_operator_1 = "*"
        test_case_2_operator_2 = "+"

        # Act
        result_test_case_1 = mathematics.greater_precedence(test_case_1_operator_1, test_case_1_operator_2)
        result_test_case_2 = mathematics.greater_precedence(test_case_2_operator_1, test_case_2_operator_2)

        # Assert
        assert result_test_case_1 == expected_test_case_1
        assert result_test_case_2 == expected_test_case_2
        