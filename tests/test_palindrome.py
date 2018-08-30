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

    def test_palindrome_from(self, tmpdir):
        """
        This checks whether the method can read list of words from a text file. Then calculate the number of palindrome in the text.
        """
        # arrange
        filepath = tmpdir.mkdir("temp").join("palindrome.txt")
        palindromes = []
        palindromes.append("Anna\n")
        palindromes.append("Amma\n")
        palindromes.append("Ada\n")
        palindromes.append("Abba\n")
        palindromes.append("Eve\n")
        palindromes.append("eYe\n")
        palindromes.append("civic\n")
        palindromes.append("pip\n")
        palindromes.append("rotator\n")
        palindromes.append("IrorI\n")

        
        palindrome_str = ''.join(palindromes)

        # output the string to the file.
        filepath.write(palindrome_str)
        expected = 10

        # act
        result = palindromechecker.palindrome_from(filepath)

        # assert
        assert result == expected
