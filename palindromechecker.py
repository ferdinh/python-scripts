import pathlib

def palindrome(word: str) -> bool:
    """
    Check if a single word is a palindrome.
    """
    reversedWord = word[::-1]

    # comparison of word
    if word.lower() != reversedWord.lower():
        return False

    return True


def palindrome_from(filepath: pathlib.Path) -> int:
    """
    Open a text file and checks for palindrome.
    """
    num_of_palindrome = 0

    # reads each line in the list of files
    with open(filepath) as file:
        content = file.readlines()

    # removes whitespace
    content = [x.strip() for x in content]

    # iterates over every word in the txt file
    for word in content:
        isPalindrome = palindrome(word)

        if isPalindrome:
            num_of_palindrome += 1

    return num_of_palindrome


def main():
    filename = input("Path to file: ")

    num_palindrome = palindrome_from(filename)

    print("There are", num_palindrome, "palindromes in this list of words")


if __name__ == "__main__":
    main()
