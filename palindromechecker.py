import pathlib
# checks if a word is a palindrome

# palindrome function


def palindrome(word: str) -> bool:
    reversedWord = word[::-1]

    # comparison of each word
    if word.lower() != reversedWord.lower():
        return False

    return True


def palindrome_from(path: pathlib.Path) -> int:
    counter = 0  # final value goes here

    # reads each line in the list of files
    with open(path) as f:
        content = f.readlines()

    # removes whitespace
    content = [x.strip() for x in content]

    # iterates over every word in the txt file
    for word in content:
        isPalindrome = palindrome(word)

        if isPalindrome:
            counter += 1

    return counter


def main():
    filename = input("Path to file: ")

    num_palindrome = palindrome_from(filename)

    print("There are", num_palindrome, "palindromes in this list of words")


if __name__ == "__main__":
    main()
