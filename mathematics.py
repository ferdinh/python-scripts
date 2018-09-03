def evaluate(expr: str) -> float:
    """
    Return the evaluation of an arithmetic expression.
    """

    rpn = parse_to_rpn(expr)
    result = evaluate_rpn(rpn)

    return result


def parse_to_rpn(expr: str) -> list:
    """
    Converts infix notation to Reverse Polish Notation (RPN).
    """
    output_stack = list()
    operator_stack = list()

    tokens = expr.split(" ")

    for token in tokens:
        buffer = 0.0

        try:
            # Send to the output stack if current 'token' is a number.
            buffer = float(token)
            output_stack.append(buffer)
        except ValueError:
            pass

        is_operator = (token == "+" or token ==
                       "-" or token == "/" or token == "*")

        if is_operator:

            operatorStackSize = len(operator_stack)

            # Check if operator stack is empty.
            operatorStackEmpty = operatorStackSize == 0

            while operatorStackSize > 0:
                # Get the last operator from the stack.
                lastOperator = operator_stack[operatorStackSize - 1]

                # If token has lower or equal precedence than the last operator in the stack
                # Pop all the operator stack and push to the output stack
                # Then add the current operator to the operator stack
                # Else, add the operator to the stack
                if (token == "+" or token == "-"):
                    if(lastOperator == "*" or lastOperator == "/" or lastOperator == "+" or lastOperator == "-"):
                        while operatorStackSize:
                            output_stack.append(operator_stack.pop())
                            operatorStackSize -= 1
                        operator_stack.append(token)
                    else:
                        operator_stack.append(token)
                        break
                else:
                    operator_stack.append(token)
                    break

            # Directly add the operator to the operator stack if empty.
            if operatorStackEmpty:
                operator_stack.append(token)

    remainingOp = len(operator_stack)

    # Push all the leftover operator to the output stack.
    if remainingOp > 0:
        while remainingOp > 0:
            output_stack.append(operator_stack.pop())
            remainingOp -= 1

    return output_stack


def evaluate_rpn(rpn: list) -> float:
    """
    Return the calculation of a given reverse polish notation (RPN)
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
                resultStack.append(
                    multiply(resultStack.pop(), resultStack.pop()))
            if token == "/":
                # Number at the end of the stack should be the denominator.
                denominator = resultStack.pop()
                numerator = resultStack.pop()
                resultStack.append(divide(numerator, denominator))

    # There should only be one number left in the stack.
    if len(resultStack) > 1:
        raise ValueError("There is a compute error when parsing the notation.")
    else:
        result = resultStack.pop()

    return result


def is_number(string: str) -> bool:
    """
    Return true if string is a number, else, false.
    """
    try:
        float(string)
        return True
    except ValueError:
        pass

    return False


def is_operator(string: str) -> bool:
    """
    Return true if it is a mathematical operator, else, false.
    """

    operators = ["+", "-", "/", "*"]

    for operator in operators:
        if operator == string:
            return True

    return False


def add(addend1: float, addend2: float) -> float:
    """
        Summation between two addends.
    """
    return addend1 + addend2


def min(subtrahend: float, minuend: float) -> float:
    """
        Return the result of subtrahend minus minuend.
    """
    return subtrahend - minuend


def multiply(multiplicand: float, multiplier: float) -> float:
    """
        Return the result of multiplicand times multiplier.
    """
    return multiplicand * multiplier


def divide(numerator: float, denominator: float) -> float:
    """
        Return the division of numerator by the denominator.
    """
    return numerator / denominator
