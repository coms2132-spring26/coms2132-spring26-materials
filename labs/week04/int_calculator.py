PRECEDENCE = {
    "~": 4,  # unary minus
    "^": 3,
    "*": 2,
    "/": 2,
    "%": 2,
    "+": 1,
    "-": 1,
}
RIGHT_ASSOC = {"^", "~"}  # ^ is right-assoc; unary minus acts like right-assoc prefix


def tokenize(expr):
    """
    Returns tokens: ints, '(', ')', operators '+-*/%^', and '~' for unary minus.
    """
    tokens = []
    expect_operand = True  # at start or after '(' or operator, we expect an operand
    i = 0
    n = len(expr)

    while i < n:
        ch = expr[i]

        if ch.isspace():
            i += 1
            continue

        if "0" <= ch <= "9":
            val = 0
            while i < n and "0" <= expr[i] <= "9":
                val = val * 10 + (int(expr[i]))
                i += 1
            tokens.append(val)
            expect_operand = False
            continue

        if ch == "(":
            tokens.append("(")
            expect_operand = True
            i += 1
            continue

        if ch == ")":
            tokens.append(")")
            expect_operand = False
            i += 1
            continue

        if ch in "+-*/%^":
            if ch == "-" and expect_operand:
                tokens.append("~")
            else:
                if expect_operand:
                    raise ValueError("Expected operand at index %d" % i)
                tokens.append(ch)
            expect_operand = True
            i += 1
            continue

        raise ValueError("Unexpected character '%s' at index %d" % (ch, i))

    if expect_operand and tokens:
        raise ValueError("Missing operand at end of expression")

    return tokens


def infix_to_postfix(tokens):
    postfix = []
    stack = [] 

    for tok in tokens:
        if isinstance(tok, int):
            postfix.append(tok)
            continue

        if tok == "(":
            stack.append(tok)
            continue

        if tok == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            if not stack:
                raise ValueError("Unmatched ')'")
            stack.pop()
            continue

        while stack and stack[-1] != "(":
            top = stack[-1]
            if (PRECEDENCE[top] > PRECEDENCE[tok]) or (
                PRECEDENCE[top] == PRECEDENCE[tok] and tok not in RIGHT_ASSOC
            ):
                postfix.append(stack.pop())
            else:
                break
        stack.append(tok)

    while stack:
        top = stack.pop()
        if top == "(":
            raise ValueError("Unmatched '('")
        postfix.append(top)

    return postfix


def eval_postfix(postfix):
    """
    Evaluate postfix expression using a stack.
    Integer-only semantics:
      - / is integer division (floor like Python //)
      - % is modulo
      - ^ is exponentiation
      - 0^0 is rejected
    """
    stack = []

    for tok in postfix:
        if isinstance(tok, int):
            stack.append(tok)
            continue

        if tok == "~":
            if not stack:
                raise ValueError("Unary minus missing operand")
            stack.append(-stack.pop())
            continue

        if len(stack) < 2:
            raise ValueError("Binary operator missing operand")

        b = stack.pop()
        a = stack.pop()

        if tok == "+":
            stack.append(a + b)
        elif tok == "-":
            stack.append(a - b)
        elif tok == "*":
            stack.append(a * b)
        elif tok == "/":
            if b == 0:
                raise ValueError("Division by zero")
            stack.append(a // b)
        elif tok == "%":
            if b == 0:
                raise ValueError("Division by zero")
            stack.append(a % b)
        elif tok == "^":
            if a == 0 and b == 0:
                raise ValueError("0^0 is undefined")
            stack.append(a ** b)
        else:
            raise ValueError("Unknown operator: %r" % tok)
        
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack.pop()


def evaluate(expr):
    tokens = tokenize(expr)
    postfix = infix_to_postfix(tokens)
    return eval_postfix(postfix)

if __name__ == "__main__":
    s = input("Enter an expression: ")
    s = s.strip()

    if len(s) == 0:
        print("No expression entered.")
    else:
        try:
            # print("Tokens:", tokenize(s))
            result = evaluate(s)
            print(f"{s} = ", result)
        except ValueError as e:
            print("Error:", e)