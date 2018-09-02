# Simple calculator script in shell
# May be extended to support other features as well as other libraries

import mathematics

def main():

    userInput = input()
    result = mathematics.evaluate(userInput)
    print(result)
    
    return 0


if __name__ == "__main__":
    main()