import sys
import os
# get the directory path of this file.
dirname = os.path.dirname(os.path.abspath(__file__))
# get the root of this child directory.
rootdir = os.path.dirname(dirname)
sys.path.append(rootdir)

import palindromechecker


class TestPalindromeClass(object):
    """
    This checks whether the method is able to check if a word is a palindrome regardless of case.
    """
    def test_palindrome(self):
        
        #arrange
        text = "Anna"
        expected = True

        #act
        result = palindromechecker.palindrome(text)

        #assert
        assert result == expected



