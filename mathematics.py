def evaluate (expr: str) -> float:

    tokens = expr.split(" ")

    x = float(tokens[0])
    operand = tokens[1]
    y = float(tokens[2])

    if operand == "+":
        result = add(x, y)
    elif operand == "-":
        result = min(x, y)
    elif operand == "*":
        result = multiply(x, y)
    elif operand == "/":
        result = divide(x, y)

    return result

def add(addend1:float , addend2: float) -> float:
    """
        Summation between two addends.
    """
    return addend1 + addend2

def min(subtrahend: float, minuend: float) -> float:
    """
        Subtracts minued from subtrahend.
    """
    return subtrahend - minuend

# Multiply two numbers.
def multiply(multiplicand: float, multiplier:float) -> float:
    """
        Performs multiplication on the multiplicand and multiplier.
    """
    return multiplicand * multiplier

def divide(numerator: float, denominator:float) -> float:
    """
        Divides the numerator to the denominator.
    """
    return numerator / denominator