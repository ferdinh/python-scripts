# Simple calculator script in shell
# May be extended to support other features as well as other libraries

import mathematics

def main():

    check = True

    while True:
        try:
            x = float(input("Enter 1st number: "))
            y = float(input("Enter 2nd number: "))
        except ValueError:
            print("Please enter a valid input!")
        else:
            break

    result = 0.0

    while check:
        choice = input("Choose an arithmetic operation (add, min, multiply, divide): ")

        if choice == "add":
            result = mathematics.add(x, y)
            check = False
        elif choice == "min":
            result = mathematics.min(x, y)
            check = False
        elif choice == "multiply":
            result = mathematics.multiply(x, y)
            check = False
        elif choice == "divide":
            result = mathematics.divide(x, y)
            check = False
        else:
            print("Please enter a valid arithmetic operation!")

    print(f"The result is {result:.3f}")
    return 0


if __name__ == "__main__":
    main()