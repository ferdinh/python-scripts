def evaluate(expr: str) -> float:
    """
    Return the evaluation of an arithmetic expression.
    """

    rpn = parse_to_rpn(expr)
    result = evaluate_rpn(rpn)

    return result


def parse_to_rpn(expression: str) -> list:
    """
    Converts infix notation to Reverse Polish Notation (RPN).
    """
    output_stack = list()
    operator_stack = list()

    tokens = expression.split(" ")

    for token in tokens:
        buffer = 0.0

        try:
            # Send to the output stack if current 'token' is a number.
            buffer = float(token)
            output_stack.append(buffer)
        except ValueError:
            pass

        if is_operator(token):

            operator_stack_size = len(operator_stack)

            # Check if operator stack is empty.
            operator_stack_empty = operator_stack_size == 0

            while operator_stack_size > 0:
                # Get the last operator from the stack.
                last_operator = operator_stack[operator_stack_size - 1]

                # If token has lower or equal precedence than the last operator in the stack
                # Pop all the operator stack and push to the output stack
                # Then add the current operator to the operator stack
                # Else, add the operator to the stack
                if (token == "+" or token == "-"):
                    if(is_operator(last_operator)):
                        while operator_stack_size:
                            output_stack.append(operator_stack.pop())
                            operator_stack_size -= 1
                        operator_stack.append(token)
                    else:
                        operator_stack.append(token)
                        break
                else:
                    operator_stack.append(token)
                    break

            # Directly add the operator to the operator stack if empty.
            if operator_stack_empty:
                operator_stack.append(token)

    remaining_operator = len(operator_stack)

    # Push all the leftover operator to the output stack.
    if remaining_operator > 0:
        while remaining_operator > 0:
            output_stack.append(operator_stack.pop())
            remaining_operator -= 1

    return output_stack


def evaluate_rpn(rpn: list) -> float:
    """
    Return the calculation of a given reverse polish notation (RPN)
    """

    # Final result will be here.
    result_stack = list()

    for token in rpn:
        # To to stack if it is a number.
        if (is_number(token)):
            result_stack.append(token)

        # Perform operation to last two operands.
        # Then push it to the stack.
        else:
            if token == "+":
                result_stack.append(add(result_stack.pop(), result_stack.pop()))
            if token == "-":
                # Number at the end of the stack should be the subtrahend.
                y = result_stack.pop()
                x = result_stack.pop()
                result_stack.append(min(x, y))
            if token == "*":
                result_stack.append(
                    multiply(result_stack.pop(), result_stack.pop()))
            if token == "/":
                # Number at the end of the stack should be the denominator.
                denominator = result_stack.pop()
                numerator = result_stack.pop()
                result_stack.append(divide(numerator, denominator))

    # There should only be one number left in the stack.
    if len(result_stack) > 1:
        raise ValueError("There is a compute error when parsing the notation.")
    else:
        result = result_stack.pop()

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
