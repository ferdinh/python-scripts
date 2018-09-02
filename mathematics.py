def evaluate(expr: str) -> float:
    """
    Evaluate and compute arithmetic expression.
    """

    rpn = parse_to_rpn(expr)
    result = evaluate_rpn(rpn)

    return result
    


def parse_to_rpn(expr: str) -> list:
    """
    Converts infix notation to Reverse Polish  Notation.
    """
    outputStack = list()
    operatorStack = list()

    tokens = expr.split(" ")

    for token in tokens:
            buffer = 0.0

            try:
                # Send to the output stack if current 'token' is a number.
                buffer = float(token)
                outputStack.append(buffer)
            except ValueError:
                pass

            isOperator = (token == "+" or token == "-" or token == "/" or token == "*")

            if isOperator:

                operatorStackSize = len(operatorStack)

                # Check if operator stack is empty.
                operatorStackEmpty = operatorStackSize == 0

                while operatorStackSize > 0:
                    # Get the last operator from the stack.
                    lastOperator = operatorStack[operatorStackSize - 1]

                    # If token has lower or equal precedence than the last operator in the stack
                    # Pop all the operator stack and push to the output stack
                    # Then add the current operator to the operator stack
                    # Else, add the operator to the stack
                    if (token == "+" or token == "-"):
                        if(lastOperator == "*" or lastOperator == "/" or lastOperator == "+" or lastOperator == "-"):
                            while operatorStackSize:
                                outputStack.append(operatorStack.pop())
                                operatorStackSize -= 1
                            operatorStack.append(token)
                        else:
                            operatorStack.append(token)
                            break
                    else:
                        operatorStack.append(token)
                        break

                # Directly add the operator to the operator stack if empty.
                if operatorStackEmpty:
                    operatorStack.append(token)

    remainingOp = len(operatorStack)

    # Push all the leftover operator to the output stack.
    if remainingOp > 0:
        while remainingOp > 0:
            outputStack.append(operatorStack.pop())
            remainingOp -= 1

    return outputStack

def evaluate_rpn(rpn: list) -> float:
    """
    Compute Reverse Polish Notation
    """

    # Final result will be here.
    resultStack = list()

    for token in rpn:
        # To to stack if it is a number.
        if (is_number(token)):
            resultStack.append(token)
        
        # Perform operation to last two operands.
        # Then push it to the stack.
        else:
            if token == "+":
                resultStack.append(add(resultStack.pop(), resultStack.pop()))
            if token == "-":
                # Number at the end of the stack should be the subtrahend.
                y = resultStack.pop()
                x = resultStack.pop()
                resultStack.append(min(x, y))
            if token == "*":
                resultStack.append(multiply(resultStack.pop(), resultStack.pop()))
            if token == "/":
                # Number at the end of the stack should be the denominator.
                denominator = resultStack.pop()
                numerator = resultStack.pop()
                resultStack.append(divide(numerator, denominator))

    # If all goes well, there should only be one data left in the stack.
    # Else, something is wrong.
    if len(resultStack) > 1:
        raise ValueError("There is a compute error when parsing the notation.")
    else:
        result = resultStack.pop()

    return result

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    return False


def add(addend1: float, addend2: float) -> float:
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


def multiply(multiplicand: float, multiplier: float) -> float:
    """
        Performs multiplication on the multiplicand and multiplier.
    """
    return multiplicand * multiplier


def divide(numerator: float, denominator: float) -> float:
    """
        Divides the numerator to the denominator.
    """
    return numerator / denominator
