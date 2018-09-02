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
        actualResult = round(mathematics.divide(self.firstNumber, self.secondNumber), 9)
            
        # assert
        assert expectedResult == actualResult

    def test_multiply(self):
        # arrange
        expectedResult = 55

        # act 
        actualResult = mathematics.multiply(self.firstNumber, self.secondNumber)

        # assert
        assert expectedResult == actualResult

    def test_parse_to_rpn(self):
        # Arrange  
        # Case 1
        expected_case_1 = [6.0, 8.0, "/", 9.0, "+", 8.0, 10.0, "*", "-"]
        infix_case_1 = "6 / 8 + 9 - 8 * 10"

        # Case 2
        expected_case_2 = [3.0, 2.0, "*", 5.0, "+"]
        infix_case_2 = "3 * 2 + 5"

        # act
        result_case_1 = mathematics.parse_to_rpn(infix_case_1)
        result_case_2 = mathematics.parse_to_rpn(infix_case_2)

        # assert
        assert result_case_1 == expected_case_1
        assert result_case_2 == expected_case_2

    def test_evaluate_rpn(self):

        #Arrange
        # Case 1
        expected_case_1 = -70.25
        infix_case_1 = [6.0, 8.0, "/", 9.0, "+", 8.0, 10.0, "*", "-"]

        # Case 2
        expected_case_2 = 11.0
        infix_case_2 = [3.0, 2.0, "*", 5.0, "+"]

        # act
        result_case_1 = mathematics.evaluate_rpn(infix_case_1)
        result_case_2 = mathematics.evaluate_rpn(infix_case_2)

        # assert
        assert result_case_1 == expected_case_1
        assert result_case_2 == expected_case_2